"""CLI entry point for auto-skill-mcp installer."""

from __future__ import annotations

import sys

from auto_skill_mcp.installer import console
from auto_skill_mcp.installer.configurator import configure_agent, uninstall_agent
from auto_skill_mcp.installer.detector import detect_global, detect_project


def _run_install(dry_run: bool = False) -> None:
    console.header("auto-skill-mcp installer")

    console.section("Detecting agents...")
    global_agents = detect_global()
    for agent in global_agents:
        path_str = str(agent.config_path) if agent.config_path else ""
        status = "exists" if agent.detected else "not_found"
        console.agent_row(agent.icon, agent.display, path_str, status)

    project_agents = detect_project()
    if project_agents:
        console.section("Project scope (current directory):")
        for agent in project_agents:
            path_str = str(agent.config_path) if agent.config_path else ""
            status = "exists" if agent.detected else "not_found"
            console.agent_row(agent.icon, agent.display, path_str, status)

    console.section("Configuring agents...")
    g_ok = 0
    for agent in global_agents:
        if not agent.config_path:
            console.result_row(agent.display, "skip", "no path")
            continue
        if not agent.config_path.parent.exists() and not agent.detected:
            console.result_row(agent.display, "skip", "agent not installed")
            continue
        msg = configure_agent(agent, dry_run=dry_run)
        if dry_run:
            console.result_row(agent.display, "ok", "would configure")
            g_ok += 1
        elif "configured" in msg:
            console.result_row(agent.display, "ok", msg)
            g_ok += 1
        else:
            console.result_row(agent.display, "skip", msg)

    console.section("Project scope files:")
    p_ok = 0
    for agent in project_agents:
        if not agent.config_path:
            console.project_row(str(agent.paths.get("all", "")), False)
            continue
        msg = configure_agent(agent, dry_run=dry_run)
        ok = dry_run or "configured" in msg
        if ok:
            p_ok += 1
        console.project_row(str(agent.config_path), ok)

    if dry_run:
        console.dry_run_box(g_ok + p_ok)
    else:
        console.summary_box(g_ok, p_ok)


def _run_uninstall() -> None:
    console.section("Removing auto-skill-mcp...")
    global_agents = detect_global()
    count = 0
    for agent in global_agents:
        if not agent.config_path or not agent.config_path.exists():
            continue
        msg = uninstall_agent(agent)
        if "removed" in msg:
            console.result_row(agent.display, "ok", msg)
            count += 1
        else:
            console.result_row(agent.display, "skip", msg)
    project_agents = detect_project()
    for agent in project_agents:
        if not agent.config_path or not agent.config_path.exists():
            continue
        msg = uninstall_agent(agent)
        if "removed" in msg:
            console.result_row(agent.display, "ok", msg)
            count += 1
        else:
            console.result_row(agent.display, "skip", msg)
    console.uninstall_summary(count)


def _run_list() -> None:
    console.section("Installed agents")
    global_agents = detect_global()
    for agent in global_agents:
        path_str = str(agent.config_path) if agent.config_path else ""
        status = "exists" if agent.detected else "not_found"
        console.agent_row(agent.icon, agent.display, path_str, status)
    project_agents = detect_project()
    if project_agents:
        console.section("Project scope (current directory):")
        for agent in project_agents:
            path_str = str(agent.config_path) if agent.config_path else ""
            status = "exists" if agent.detected else "not_found"
            console.agent_row(agent.icon, agent.display, path_str, status)


def main() -> None:
    """Main entry point. Routes to installer or MCP server."""
    args = [a.lower() for a in sys.argv[1:]]

    if not args:
        from auto_skill_mcp.server import main as server_main

        server_main()
        return

    cmd = args[0]

    if cmd == "install":
        dry_run = "--dry-run" in args or "-n" in args
        _run_install(dry_run=dry_run)
    elif cmd == "uninstall":
        _run_uninstall()
    elif cmd == "list":
        _run_list()
    elif cmd in ("--help", "-h"):
        print("Usage:")
        print("  auto-skill-mcp              Start MCP server")
        print("  auto-skill-mcp install      Install to all detected agents")
        print("  auto-skill-mcp install --dry-run  Preview only")
        print("  auto-skill-mcp uninstall    Remove from all agents")
        print("  auto-skill-mcp list         Show detected agents")
    else:
        from auto_skill_mcp.server import main as server_main

        server_main()


if __name__ == "__main__":
    main()
