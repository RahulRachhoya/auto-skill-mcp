"""Tests for the auto-skill-mcp installer module."""

from __future__ import annotations

import json
from pathlib import Path

from auto_skill_mcp.installer.configurator import (
    OK,
    SKIP,
    WOULD,
    _backup,
    _entry_for,
    _merge_via_mcp_servers,
    _merge_via_opencode,
    _opencode_servers,
    _read_json,
    _write_json_atomic,
    configure_agent,
    uninstall_agent,
)
from auto_skill_mcp.installer.detector import Agent, detect_project


def _agent(**overrides: object) -> Agent:
    defaults: dict[str, object] = {
        "name": "test-agent",
        "display": "Test Agent",
        "icon": "T",
        "root_key": "mcpServers",
        "needs_type": False,
        "scope": "global",
        "paths": {"win32": "/tmp/test.json", "darwin": "/tmp/test.json", "linux": "/tmp/test.json"},
    }
    defaults.update(overrides)
    return Agent(**defaults)  # type: ignore[arg-type]


class TestReadJson:
    def test_missing_file(self, tmp_path: Path) -> None:
        p = tmp_path / "missing.json"
        assert _read_json(p) == {}

    def test_valid_json(self, tmp_path: Path) -> None:
        p = tmp_path / "config.json"
        p.write_text('{"a": 1}', encoding="utf-8")
        assert _read_json(p) == {"a": 1}

    def test_empty_file(self, tmp_path: Path) -> None:
        p = tmp_path / "empty.json"
        p.write_text("", encoding="utf-8")
        assert _read_json(p) == {}

    def test_malformed_json(self, tmp_path: Path) -> None:
        p = tmp_path / "bad.json"
        p.write_text("{broken", encoding="utf-8")
        assert _read_json(p) == {}


class TestWriteJsonAtomic:
    def test_writes_json(self, tmp_path: Path) -> None:
        p = tmp_path / "out.json"
        _write_json_atomic(p, {"key": "val"})
        assert json.loads(p.read_text(encoding="utf-8")) == {"key": "val"}

    def test_creates_parent_dirs(self, tmp_path: Path) -> None:
        p = tmp_path / "a" / "b" / "out.json"
        _write_json_atomic(p, {"x": 1})
        assert p.exists()

    def test_overwrites_existing(self, tmp_path: Path) -> None:
        p = tmp_path / "out.json"
        p.write_text('{"old": 1}', encoding="utf-8")
        _write_json_atomic(p, {"new": 2})
        assert json.loads(p.read_text(encoding="utf-8")) == {"new": 2}


class TestBackup:
    def test_creates_backup(self, tmp_path: Path) -> None:
        p = tmp_path / "config.json"
        p.write_text('{"a": 1}', encoding="utf-8")
        bak = _backup(p)
        assert bak is not None
        assert bak.exists()
        assert ".bak." in bak.name
        assert bak.name.startswith("config.json.bak.")

    def test_missing_file_returns_none(self, tmp_path: Path) -> None:
        p = tmp_path / "missing.json"
        assert _backup(p) is None


class TestEntryFor:
    def test_basic_entry(self) -> None:
        agent = _agent(needs_type=False)
        entry = _entry_for(agent)
        assert entry["command"] == "uvx"
        assert entry["args"] == ["auto-skill-mcp"]
        assert "type" not in entry

    def test_needs_type(self) -> None:
        agent = _agent(needs_type=True)
        entry = _entry_for(agent)
        assert entry["type"] == "stdio"


class TestMergeViaMcpServers:
    def test_merges_into_empty(self) -> None:
        config: dict[str, object] = {}
        result = _merge_via_mcp_servers(config, "mcpServers", {"command": "uvx", "args": ["test"]})
        servers = result["mcpServers"]
        assert isinstance(servers, dict)
        assert servers["auto-skill-mcp"] == {"command": "uvx", "args": ["test"]}

    def test_preserves_existing_servers(self) -> None:
        config: dict[str, object] = {"mcpServers": {"existing-tool": {"command": "foo"}}}
        result = _merge_via_mcp_servers(config, "mcpServers", {"command": "uvx", "args": ["test"]})
        servers = result["mcpServers"]
        assert isinstance(servers, dict)
        assert "existing-tool" in servers
        assert "auto-skill-mcp" in servers

    def test_overwrites_existing_entry(self) -> None:
        old = {"command": "old"}
        config: dict[str, object] = {"mcpServers": {"auto-skill-mcp": old}}
        result = _merge_via_mcp_servers(config, "mcpServers", {"command": "new"})
        servers = result["mcpServers"]
        assert isinstance(servers, dict)
        assert servers["auto-skill-mcp"] == {"command": "new"}


class TestMergeViaOpencode:
    def test_merges_into_empty(self) -> None:
        config: dict[str, object] = {}
        entry: dict[str, object] = {"command": "uvx", "args": ["test"]}
        result = _merge_via_opencode(config, entry)
        mcp = result["mcp"]
        assert isinstance(mcp, dict)
        servers = mcp.get("servers")
        assert isinstance(servers, list)
        assert servers[-1]["name"] == "auto-skill-mcp"

    def test_preserves_existing(self) -> None:
        config: dict[str, object] = {"mcp": {"servers": [{"name": "other-tool", "command": "foo"}]}}
        entry: dict[str, object] = {"command": "uvx", "args": ["test"]}
        result = _merge_via_opencode(config, entry)
        servers = result["mcp"]["servers"]  # type: ignore[index]
        assert isinstance(servers, list)
        assert len(servers) == 2
        assert servers[0]["name"] == "other-tool"
        assert servers[1]["name"] == "auto-skill-mcp"

    def test_replaces_existing_entry(self) -> None:
        config: dict[str, object] = {
            "mcp": {"servers": [{"name": "auto-skill-mcp", "command": "old"}]}
        }
        entry: dict[str, object] = {"command": "new", "args": ["test"]}
        result = _merge_via_opencode(config, entry)
        servers = result["mcp"]["servers"]  # type: ignore[index]
        assert isinstance(servers, list)
        assert len(servers) == 1
        assert servers[0]["command"] == "new"

    def test_handles_malformed_servers(self) -> None:
        config: dict[str, object] = {"mcp": {"servers": "not-a-list"}}
        entry: dict[str, object] = {"command": "uvx", "args": ["test"]}
        result = _merge_via_opencode(config, entry)
        servers = result["mcp"]["servers"]  # type: ignore[index]
        assert isinstance(servers, list)
        assert len(servers) == 1


class TestOpencodeServers:
    def test_removes_entry(self) -> None:
        config: dict[str, object] = {
            "mcp": {"servers": [{"name": "auto-skill-mcp"}, {"name": "other"}]}
        }
        mcp = _opencode_servers(config)
        servers = mcp.get("servers", [])
        assert isinstance(servers, list)
        names = [s["name"] for s in servers]  # type: ignore[index]
        assert names == ["other"]

    def test_returns_empty_servers_when_no_mcp_key(self) -> None:
        mcp = _opencode_servers({})
        assert mcp.get("servers") == []


class TestConfigureAgent:
    def test_skip_no_path(self) -> None:
        agent = _agent(config_path=None)
        status, msg = configure_agent(agent)
        assert status == SKIP
        assert msg == "no path"

    def test_skip_missing_parent(self, tmp_path: Path) -> None:
        agent = _agent(config_path=tmp_path / "nonexistent" / "config.json")
        status, msg = configure_agent(agent)
        assert status == SKIP
        assert "parent dir missing" in msg

    def test_would_configure(self, tmp_path: Path) -> None:
        p = tmp_path / "config.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("{}", encoding="utf-8")
        agent = _agent(config_path=p)
        status, msg = configure_agent(agent, dry_run=True)
        assert status == WOULD

    def test_configures_agent(self, tmp_path: Path) -> None:
        p = tmp_path / "config.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("{}", encoding="utf-8")
        agent = _agent(config_path=p)
        status, msg = configure_agent(agent)
        assert status == OK
        config = json.loads(p.read_text(encoding="utf-8"))
        assert "auto-skill-mcp" in config["mcpServers"]

    def test_configures_opencode(self, tmp_path: Path) -> None:
        p = tmp_path / "opencode.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("{}", encoding="utf-8")
        agent = _agent(name="opencode", config_path=p, root_key="mcp")
        status, msg = configure_agent(agent)
        assert status == OK
        config = json.loads(p.read_text(encoding="utf-8"))
        servers = config["mcp"]["servers"]
        assert isinstance(servers, list)
        assert servers[0]["name"] == "auto-skill-mcp"

    def test_creates_backup(self, tmp_path: Path) -> None:
        p = tmp_path / "config.json"
        p.write_text('{"other": {}}', encoding="utf-8")
        agent = _agent(config_path=p)
        configure_agent(agent)
        backups = list(tmp_path.glob("config.json.bak.*"))
        assert len(backups) == 1


class TestUninstallAgent:
    def test_skip_not_found(self) -> None:
        agent = _agent(config_path=None)
        status, msg = uninstall_agent(agent)
        assert status == SKIP

    def test_would_remove(self, tmp_path: Path) -> None:
        p = tmp_path / "config.json"
        p.write_text("{}", encoding="utf-8")
        agent = _agent(config_path=p)
        status, msg = uninstall_agent(agent, dry_run=True)
        assert status == WOULD

    def test_removes_mcp_servers_entry(self, tmp_path: Path) -> None:
        data = {"mcpServers": {"auto-skill-mcp": {"command": "uvx"}, "other": {"command": "foo"}}}
        p = tmp_path / "config.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        agent = _agent(config_path=p)
        status, msg = uninstall_agent(agent)
        assert status == OK
        config = json.loads(p.read_text(encoding="utf-8"))
        assert "auto-skill-mcp" not in config["mcpServers"]
        assert "other" in config["mcpServers"]

    def test_removes_opencode_entry(self, tmp_path: Path) -> None:
        data = {
            "mcp": {
                "servers": [
                    {"name": "auto-skill-mcp"},
                    {"name": "other-tool"},
                ]
            }
        }
        p = tmp_path / "opencode.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        agent = _agent(name="opencode", config_path=p, root_key="mcp")
        status, msg = uninstall_agent(agent)
        assert status == OK
        config = json.loads(p.read_text(encoding="utf-8"))
        servers = config["mcp"]["servers"]
        assert isinstance(servers, list)
        assert len(servers) == 1
        assert servers[0]["name"] == "other-tool"

    def test_removes_nothing_when_not_present(self, tmp_path: Path) -> None:
        data = {"mcpServers": {"other": {"command": "foo"}}}
        p = tmp_path / "config.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        agent = _agent(config_path=p)
        status, msg = uninstall_agent(agent)
        assert status == OK


class TestDetectProject:
    def test_returns_agent_list(self, tmp_path: Path) -> None:
        agents = detect_project(cwd=tmp_path)
        assert len(agents) == 4
        assert all(a.scope == "project" for a in agents)

    def test_detects_vscode_config(self, tmp_path: Path) -> None:
        vscode_dir = tmp_path / ".vscode"
        vscode_dir.mkdir()
        (vscode_dir / "mcp.json").write_text("{}", encoding="utf-8")
        agents = detect_project(cwd=tmp_path)
        vscode = [a for a in agents if a.name == "vscode"][0]
        assert vscode.detected is True
