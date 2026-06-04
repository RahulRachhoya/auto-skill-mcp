"""Minimal console renderer for auto-skill-mcp installer."""

from __future__ import annotations

import os
import sys


class Color:
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    GRAY = "\033[90m"


def _init_ansi() -> None:
    if sys.platform == "win32":
        os.system("")


def header(text: str) -> None:
    sep = Color.DIM + "=" * 50 + Color.RESET
    print()
    print(sep)
    print(Color.BOLD + f"  {text}" + Color.RESET)
    print(sep)
    print()


def section(title: str) -> None:
    print()
    print(Color.BOLD + Color.CYAN + f"> {title}" + Color.RESET)
    print()


def agent_row(icon: str, name: str, path: str, status: str) -> None:
    status_char, status_color = {
        "configured": ("+", Color.GREEN),
        "not_found": ("-", Color.RED),
        "exists": ("o", Color.YELLOW),
    }.get(status, ("?", Color.GRAY))
    p = path if path else Color.GRAY + "not found" + Color.RESET
    line = f"  {icon} {Color.BOLD}{name:<18}{Color.RESET}"
    line += f" {Color.GRAY}{p}{Color.RESET}  [{status_color}{status_char}{Color.RESET}]"
    print(line)


def result_row(name: str, status: str, detail: str = "") -> None:
    ok = status == "ok"
    icon = Color.GREEN + "+" + Color.RESET if ok else Color.RED + "x" + Color.RESET
    icon_mid = Color.YELLOW + "-" + Color.RESET if status == "skip" else icon
    padded = f"{name:<20}"
    detail_str = f"  {Color.GRAY}-> {detail}{Color.RESET}" if detail else ""
    print(f"  {icon_mid}  {Color.BOLD}{padded}{Color.RESET}{detail_str}")


def project_row(path: str, status: bool) -> None:
    icon = Color.GREEN + "+" + Color.RESET if status else Color.RED + "x" + Color.RESET
    label = "auto-skill-mcp " + ["skipped", "added"][status]
    print(f"  {icon}  {Color.BOLD}{path:<22}{Color.RESET}  {Color.GRAY}{label}{Color.RESET}")


def summary_box(agents_count: int, project_count: int) -> None:
    print()
    print(Color.GREEN + Color.BOLD + "  auto-skill-mcp ready" + Color.RESET)
    print(f"  Installed to {agents_count} agent{'s' if agents_count != 1 else ''}")
    if project_count:
        print(f"  + {project_count} project scope file{'s' if project_count != 1 else ''}")
    print(Color.GRAY + "  Restart your coding tools to activate" + Color.RESET)
    print()


def dry_run_box(agents_count: int) -> None:
    print()
    print(Color.YELLOW + Color.BOLD + "  DRY RUN — no files were written" + Color.RESET)
    print(f"  {agents_count} agent(s) would be configured")
    print()


def uninstall_summary(count: int) -> None:
    print()
    print(Color.MAGENTA + Color.BOLD + "  auto-skill-mcp removed" + Color.RESET)
    print(f"  Removed from {count} config(s)")
    print()


_init_ansi()
