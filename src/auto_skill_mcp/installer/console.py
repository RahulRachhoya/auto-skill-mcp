"""8-bit retro console renderer for auto-skill-mcp installer."""

from __future__ import annotations

import os
import shutil
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
    ORANGE = "\033[38;5;208m"

    @classmethod
    def rgb(cls, r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"


PIXEL_LOGO = [
    "  "
    + Color.rgb(0, 200, 255)
    + "▄▀▀▄"
    + Color.GRAY
    + " "
    + Color.rgb(255, 100, 200)
    + "▄▀▀▄"
    + Color.GRAY
    + " "
    + Color.rgb(255, 200, 50)
    + "▄▀▀▀▀"
    + Color.RESET,
    "  "
    + Color.rgb(0, 200, 255)
    + "█  ██"
    + Color.GRAY
    + " "
    + Color.rgb(255, 100, 200)
    + "██ █"
    + Color.GRAY
    + " "
    + Color.rgb(255, 200, 50)
    + "██  ██"
    + Color.RESET,
    "  "
    + Color.rgb(0, 200, 255)
    + "█  ██"
    + Color.GRAY
    + " "
    + Color.rgb(255, 100, 200)
    + "██ █"
    + Color.GRAY
    + " "
    + Color.rgb(255, 200, 50)
    + "████"
    + Color.RESET
    + "   "
    + Color.ORANGE
    + "★ ★ ★"
    + Color.RESET,
    "  "
    + Color.rgb(0, 200, 255)
    + "█  ██"
    + Color.GRAY
    + " "
    + Color.rgb(255, 100, 200)
    + "██ █"
    + Color.GRAY
    + " "
    + Color.rgb(255, 200, 50)
    + "██  ██"
    + Color.RESET,
    "  "
    + Color.rgb(0, 200, 255)
    + " ▀▀"
    + Color.GRAY
    + "  "
    + Color.rgb(255, 100, 200)
    + " ▀▀"
    + Color.GRAY
    + "  "
    + Color.rgb(255, 200, 50)
    + "██  ██"
    + Color.RESET,
]


def _init_ansi() -> None:
    if sys.platform == "win32":
        os.system("")
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]


def _term_width() -> int:
    return shutil.get_terminal_size().columns


def _center(text: str) -> str:
    w = _term_width()
    stripped = _strip_ansi(text)
    pad = max(0, (w - len(stripped)) // 2)
    return " " * pad + text


def logo() -> None:
    for line in PIXEL_LOGO:
        print(_center(line))


def header(text: str) -> None:
    w = _term_width() - 4
    inner = f" {text} ".center(w, "═")
    print(Color.DIM + "╔" + "═" * w + "╗" + Color.RESET)
    print(Color.DIM + "║" + Color.RESET + " " * w + Color.DIM + "║" + Color.RESET)
    for line in PIXEL_LOGO:
        print(
            Color.DIM
            + "║"
            + Color.RESET
            + " " * ((w - len(_strip_ansi(line))) // 2)
            + line
            + " " * ((w - len(_strip_ansi(line)) + 1) // 2)
            + Color.DIM
            + "║"
            + Color.RESET
        )
    print(Color.DIM + "║" + Color.RESET + " " * w + Color.DIM + "║" + Color.RESET)
    print(
        Color.DIM
        + "║"
        + Color.RESET
        + Color.BOLD
        + inner
        + Color.RESET
        + Color.DIM
        + "║"
        + Color.RESET
    )
    tag = "universal skill installer".center(w)
    print(
        Color.DIM
        + "║"
        + Color.RESET
        + Color.GRAY
        + tag
        + Color.RESET
        + Color.DIM
        + "║"
        + Color.RESET
    )
    print(Color.DIM + "╚" + "═" * w + "╝" + Color.RESET + Color.RESET)


def _strip_ansi(text: str) -> str:
    import re

    return re.sub(r"\033\[[0-9;]*m", "", text)


def section(title: str) -> None:
    print()
    print(Color.BOLD + Color.CYAN + "  ◆ " + title + Color.RESET)
    print()


def agent_row(icon: str, name: str, path: str, status: str) -> None:
    status_char, status_color = {
        "configured": ("✔", Color.GREEN),
        "not_found": ("–", Color.RED),
        "exists": ("○", Color.YELLOW),
    }.get(status, ("?", Color.GRAY))
    p = path if path else Color.GRAY + "not found" + Color.RESET
    line = f"  {icon} {Color.BOLD}{name:<18}{Color.RESET} {Color.GRAY}{p}{Color.RESET}"
    line += f"  {status_color}{status_char}{Color.RESET}"
    print(line)


def result_row(name: str, status: str, detail: str = "") -> None:
    ok = status == "ok"
    icon = Color.GREEN + "✔" + Color.RESET if ok else Color.RED + "✘" + Color.RESET
    icon_mid = Color.YELLOW + "–" + Color.RESET if status == "skip" else icon
    padded = f"{name:<20}"
    detail_str = f"  {Color.GRAY}→ {detail}{Color.RESET}" if detail else ""
    print(f"  {icon_mid}  {Color.BOLD}{padded}{Color.RESET}{detail_str}")


def project_row(path: str, status: bool) -> None:
    icon = Color.GREEN + "✔" + Color.RESET if status else Color.RED + "✘" + Color.RESET
    label = "auto-skill-mcp " + ["skipped", "added"][status]
    print(f"  {icon}  {Color.BOLD}{path:<22}{Color.RESET}  {Color.GRAY}{label}{Color.RESET}")


def summary_box(agents_count: int, project_count: int) -> None:
    w = _term_width() - 4
    print()
    print(Color.CYAN + "╔" + "═" * w + "╗" + Color.RESET)
    print(Color.CYAN + "║" + Color.RESET + " " * w + Color.CYAN + "║" + Color.RESET)
    text = "★  ★  auto-skill-mcp ready  ★  ★"
    print(
        Color.CYAN
        + "║"
        + Color.RESET
        + " " * ((w - len(text)) // 2)
        + Color.BOLD
        + Color.YELLOW
        + text
        + Color.RESET
        + " " * ((w - len(text) + 1) // 2)
        + Color.CYAN
        + "║"
        + Color.RESET
    )
    print(Color.CYAN + "║" + Color.RESET + " " * w + Color.CYAN + "║" + Color.RESET)
    info = f"Installed to {agents_count} agent{'s' if agents_count != 1 else ''}"
    print(
        Color.CYAN
        + "║"
        + Color.RESET
        + " " * ((w - len(info)) // 2)
        + Color.GREEN
        + info
        + Color.RESET
        + " " * ((w - len(info) + 1) // 2)
        + Color.CYAN
        + "║"
        + Color.RESET
    )
    if project_count:
        p_info = f"+ {project_count} project scope file{'s' if project_count != 1 else ''}"
        print(
            Color.CYAN
            + "║"
            + Color.RESET
            + " " * ((w - len(p_info)) // 2)
            + Color.GRAY
            + p_info
            + Color.RESET
            + " " * ((w - len(p_info) + 1) // 2)
            + Color.CYAN
            + "║"
            + Color.RESET
        )
    print(Color.CYAN + "║" + Color.RESET + " " * w + Color.CYAN + "║" + Color.RESET)
    restart = "Restart your coding tools to activate"
    print(
        Color.CYAN
        + "║"
        + Color.RESET
        + " " * ((w - len(restart)) // 2)
        + Color.GRAY
        + restart
        + Color.RESET
        + " " * ((w - len(restart) + 1) // 2)
        + Color.CYAN
        + "║"
        + Color.RESET
    )
    print(Color.CYAN + "╚" + "═" * w + "╝" + Color.RESET)
    print()


def dry_run_box(agents_count: int) -> None:
    print()
    print(Color.YELLOW + "  ╔══════════════════════════════════════╗" + Color.RESET)
    print(
        Color.YELLOW
        + "  ║"
        + Color.RESET
        + "  "
        + Color.BOLD
        + "DRY RUN — no files were written"
        + Color.RESET
        + "   "
        + Color.YELLOW
        + "║"
        + Color.RESET
    )
    print(
        Color.YELLOW
        + "  ║"
        + Color.RESET
        + f"  {agents_count} agent(s) would be configured       "
        + Color.YELLOW
        + "║"
        + Color.RESET
    )
    print(Color.YELLOW + "  ╚══════════════════════════════════════╝" + Color.RESET)
    print()


def uninstall_summary(count: int) -> None:
    print()
    print(Color.MAGENTA + "  ╔══════════════════════════════════════╗" + Color.RESET)
    print(
        Color.MAGENTA
        + "  ║"
        + Color.RESET
        + "  "
        + Color.BOLD
        + "auto-skill-mcp removed"
        + Color.RESET
        + "             "
        + Color.MAGENTA
        + "║"
        + Color.RESET
    )
    print(
        Color.MAGENTA
        + "  ║"
        + Color.RESET
        + f"  Removed from {count} config(s)               "
        + Color.MAGENTA
        + "║"
        + Color.RESET
    )
    print(Color.MAGENTA + "  ╚══════════════════════════════════════╝" + Color.RESET)
    print()


_init_ansi()
