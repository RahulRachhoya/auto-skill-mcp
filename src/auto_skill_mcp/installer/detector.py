"""Cross-platform agent detection for auto-skill-mcp installer."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal


@dataclass
class Agent:
    name: str
    display: str
    icon: str
    root_key: str
    needs_type: bool
    scope: Literal["global", "project"]
    paths: dict[str, str] = field(default_factory=dict)
    config_path: Path | None = None
    detected: bool = False


GLOBAL_AGENTS: list[Agent] = [
    Agent(
        name="claude-desktop",
        display="Claude Desktop",
        icon="\U0001f5a5",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "%APPDATA%/Claude/claude_desktop_config.json",
            "darwin": "~/Library/Application Support/Claude/claude_desktop_config.json",
            "linux": "~/.config/Claude/claude_desktop_config.json",
        },
    ),
    Agent(
        name="claude-code",
        display="Claude Code",
        icon="\u2606",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "~/.claude.json",
            "darwin": "~/.claude.json",
            "linux": "~/.claude.json",
        },
    ),
    Agent(
        name="cursor",
        display="Cursor",
        icon="\u25b6",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "~/.cursor/mcp.json",
            "darwin": "~/.cursor/mcp.json",
            "linux": "~/.cursor/mcp.json",
        },
    ),
    Agent(
        name="windsurf",
        display="Windsurf",
        icon="\u25c6",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "~/.codeium/windsurf/mcp_config.json",
            "darwin": "~/.codeium/windsurf/mcp_config.json",
            "linux": "~/.codeium/windsurf/mcp_config.json",
        },
    ),
    Agent(
        name="cline",
        display="Cline",
        icon="\u25cb",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "%APPDATA%/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json",  # noqa: E501
            "darwin": "~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json",  # noqa: E501
            "linux": "~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json",  # noqa: E501
        },
    ),
    Agent(
        name="roo-code",
        display="Roo Code",
        icon="\u25c7",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "%APPDATA%/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json",  # noqa: E501
            "darwin": "~/Library/Application Support/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json",  # noqa: E501
            "linux": "~/.config/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json",  # noqa: E501
        },
    ),
    Agent(
        name="opencode",
        display="OpenCode",
        icon="\u25a3",
        root_key="mcp",
        needs_type=False,
        scope="global",
        paths={
            "win32": "%USERPROFILE%/.config/opencode/settings.json",
            "darwin": "~/.config/opencode/settings.json",
            "linux": "~/.config/opencode/settings.json",
        },
    ),
    Agent(
        name="gemini-cli",
        display="Gemini CLI",
        icon="\u2601",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "~/.gemini/settings.json",
            "darwin": "~/.gemini/settings.json",
            "linux": "~/.gemini/settings.json",
        },
    ),
    Agent(
        name="copilot-cli",
        display="GitHub Copilot CLI",
        icon="\u2661",
        root_key="mcpServers",
        needs_type=False,
        scope="global",
        paths={
            "win32": "~/.copilot/mcp-config.json",
            "darwin": "~/.copilot/mcp-config.json",
            "linux": "~/.copilot/mcp-config.json",
        },
    ),
]

PROJECT_AGENTS: list[Agent] = [
    Agent(
        name="claude-code-project",
        display="Claude Code (project)",
        icon="\u2606",
        root_key="mcpServers",
        needs_type=False,
        scope="project",
        paths={"all": ".mcp.json"},
    ),
    Agent(
        name="cursor-project",
        display="Cursor (project)",
        icon="\u25b6",
        root_key="mcpServers",
        needs_type=False,
        scope="project",
        paths={"all": ".cursor/mcp.json"},
    ),
    Agent(
        name="vscode",
        display="VS Code",
        icon="\u25a0",
        root_key="servers",
        needs_type=True,
        scope="project",
        paths={"all": ".vscode/mcp.json"},
    ),
    Agent(
        name="jetbrains",
        display="JetBrains AI",
        icon="\u25c8",
        root_key="mcpServers",
        needs_type=False,
        scope="project",
        paths={"all": ".idea/mcp.json"},
    ),
]


def _resolve(path_template: str) -> Path:
    """Resolve a path template to an absolute Path on the current OS."""
    if sys.platform == "win32":
        # Expand %APPDATA%, %USERPROFILE% on Windows
        path_template = os.path.expandvars(path_template)
    path_template = os.path.expanduser(path_template)
    p = Path(path_template)
    return p


def detect_global() -> list[Agent]:
    """Detect which global agents have config files on this system."""
    platform = sys.platform
    found: list[Agent] = []
    for agent in GLOBAL_AGENTS:
        pt = agent.paths.get(platform) or agent.paths.get("linux") or agent.paths.get("darwin")
        if pt is None:
            continue
        resolved = _resolve(pt)
        agent.config_path = resolved
        agent.detected = resolved.exists()
        found.append(agent)
    return found


def detect_project(cwd: Path | None = None) -> list[Agent]:
    """Detect project-scope agents relative to cwd."""
    cwd = cwd or Path.cwd()
    found: list[Agent] = []
    for agent in PROJECT_AGENTS:
        pt = agent.paths.get("all")
        if pt is None:
            continue
        resolved = (cwd / pt).resolve()
        agent.config_path = resolved
        agent.detected = resolved.exists()
        found.append(agent)
    return found
