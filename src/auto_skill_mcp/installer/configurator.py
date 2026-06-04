"""Safe config file manipulation for auto-skill-mcp installer."""

from __future__ import annotations

import json
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path
from typing import cast

from auto_skill_mcp.installer.detector import Agent

SERVER_ENTRY: dict[str, object] = {
    "command": "uvx",
    "args": ["auto-skill-mcp"],
}


def _entry_for(agent: Agent) -> dict[str, object]:
    """Build the server entry for a given agent, handling format quirks."""
    entry = dict(SERVER_ENTRY)
    if agent.needs_type:
        entry["type"] = "stdio"
    return entry


def _backup(path: Path) -> Path | None:
    """Create a .bak copy of the config file. Returns backup path or None."""
    if not path.exists():
        return None
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    bak = path.with_suffix(path.suffix + f".bak.{ts}")
    shutil.copy2(path, bak)
    return bak


def _read_json(path: Path) -> dict[str, object]:
    """Read a JSON config file, returning empty dict if not found."""
    if not path.exists():
        return {}
    return cast(dict[str, object], json.loads(path.read_text(encoding="utf-8")))


def _write_json_atomic(path: Path, data: dict[str, object]) -> None:
    """Write JSON atomically using a temp file + rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _merge_via_mcp_servers(
    config: dict[str, object],
    root_key: str,
    entry: dict[str, object],
) -> dict[str, object]:
    """Merge entry into config using mcpServers-style dict format."""
    servers: dict[str, object] = {}
    existing = config.get(root_key, {})
    if isinstance(existing, dict):
        servers = dict(existing)
    servers["auto-skill-mcp"] = entry
    config[root_key] = servers
    return config


def _merge_via_opencode(
    config: dict[str, object],
    entry: dict[str, object],
) -> dict[str, object]:
    """Merge entry into OpenCode's array-based format."""
    mcp_raw = config.get("mcp", {})
    mcp: dict[str, object] = cast(dict[str, object], mcp_raw) if isinstance(mcp_raw, dict) else {}
    servers_list: list[dict[str, object]] = []
    existing = mcp.get("servers", [])
    if isinstance(existing, list):
        servers_list = [
            s for s in existing if not (isinstance(s, dict) and s.get("name") == "auto-skill-mcp")
        ]
    servers_list.append(
        {
            "name": "auto-skill-mcp",
            "transport": "stdio",
            "command": entry["command"],
            "args": entry["args"],
            "enabled": True,
        }
    )
    mcp["servers"] = servers_list
    config["mcp"] = mcp
    return config


def configure_agent(agent: Agent, dry_run: bool = False) -> str:
    """Add auto-skill-mcp to a single agent's config file.

    Returns a status message.
    """
    path = agent.config_path
    if path is None:
        return "no path"

    if not path.parent.exists():
        return "parent dir missing"

    entry = _entry_for(agent)

    if dry_run:
        return "would configure"

    bak = _backup(path)
    config = _read_json(path)

    if agent.name == "opencode":
        config = _merge_via_opencode(config, entry)
    else:
        config = _merge_via_mcp_servers(config, agent.root_key, entry)

    _write_json_atomic(path, config)
    return "configured" + (f" (backup: {bak.name})" if bak else "")


def uninstall_agent(agent: Agent, dry_run: bool = False) -> str:
    """Remove auto-skill-mcp from a single agent's config file."""
    path = agent.config_path
    if path is None or not path.exists():
        return "not found"

    if dry_run:
        return "would remove"

    bak = _backup(path)
    config = _read_json(path)

    if agent.name == "opencode":
        mcp_raw = config.get("mcp", {})
        mcp: dict[str, object] = (
            cast(dict[str, object], mcp_raw) if isinstance(mcp_raw, dict) else {}
        )
        servers_list: list[dict[str, object]] = []
        existing = mcp.get("servers", [])
        if isinstance(existing, list):
            servers_list = [
                s
                for s in existing
                if not (isinstance(s, dict) and s.get("name") == "auto-skill-mcp")
            ]
        mcp["servers"] = servers_list
        config["mcp"] = mcp
    else:
        root = config.get(agent.root_key, {})
        if isinstance(root, dict):
            root.pop("auto-skill-mcp", None)

    _write_json_atomic(path, config)
    return "removed" + (f" (backup: {bak.name})" if bak else "")
