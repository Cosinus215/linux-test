"""
Qtile Configuration — Windows 10 Inspired Minimal Setup
========================================================

Principles:
  - No tiling: all windows float freely (like a traditional desktop).
  - Single desktop (no virtual desktop switching).
  - Bottom taskbar with: start button → taskbar window buttons → tray → clock.
  - rofi (Super+R / Start button) acts as the application launcher.
  - Always-visible window borders (focused = blue, unfocused = dark).

Keybindings
-----------
  Super+Return    terminal
  Super+R         rofi (app launcher / start menu)
  Alt+F4          close focused window
  Super+Up        toggle maximize
  Super+Down      minimize
  F11             toggle fullscreen
  Super+Q         quit qtile (also terminates X server)
  Super+Shift+R   reload config
  Super+Ctrl+R    restart qtile
  Alt+Tab         cycle windows
  Alt+Shift+Tab   cycle windows (reverse)

Mouse
-----
  Super+drag       move floating window
  Super+right-drag resize floating window
  Super+middle-click bring window to front

Window decorations:
  Borders are drawn by Qtile (blue focus, dark unfocused).
  Qtile deliberately does NOT draw per-window titlebars with buttons
  (confirmed design limitation).  Many apps draw their own via CSD —
  .xinitrc sets GTK_CSD=1 for GTK apps; Qt apps (konsole, dolphin, kate)
  auto-use CSD when the WM provides no server-side decorations.
"""

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

mod = "mod4"  # Super / Windows key

# ---------------------------------------------------------------------------
# Keybindings
# ---------------------------------------------------------------------------
keys = [
    # Terminal
    Key([mod], "Return", lazy.spawn("konsole")),
    # Application launcher (rofi acts as the start menu)
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    # Close focused window (Alt+F4 — Windows standard)
    Key(["mod1"], "F4", lazy.window.kill()),
    # Toggle maximize
    Key([mod], "Up", lazy.window.toggle_maximize()),
    # Minimize
    Key([mod], "Down", lazy.window.minimize()),
    # Toggle fullscreen
    Key([], "F11", lazy.window.toggle_fullscreen()),
    # Quit qtile (which terminates X server since startx exec's it)
    Key([mod], "q", lazy.shutdown()),
    # Reload config without restarting
    Key([mod, "shift"], "r", lazy.reload_config()),
    # Full restart
    Key([mod, "control"], "r", lazy.restart()),
    # Window cycling (Alt+Tab style)
    Key(["mod1"], "Tab", lazy.layout.next()),
    Key(["mod1", "shift"], "Tab", lazy.layout.previous()),
]

# ---------------------------------------------------------------------------
# Single desktop group (no virtual desktop switching)
# ---------------------------------------------------------------------------
groups = [Group("default")]

# ---------------------------------------------------------------------------
# Layouts — all windows are inherently floating.
# Use layout.Floating instead of a tiling layout + force-float hook.
# ---------------------------------------------------------------------------
layouts = [
    layout.Floating(
        border_focus="#ff0000",    # TEMP: bright red for testing
        border_normal="#00ff00",   # TEMP: bright green for testing
        border_width=5,            # TEMP: thick to confirm borders work
    )
]

# Floating window appearance (also controls windows matching float_rules)
floating_layout = layout.Floating(
    border_focus="#ff0000",
    border_normal="#00ff00",
    border_width=5,
)

# ---------------------------------------------------------------------------
# Mouse behaviour
# ---------------------------------------------------------------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart"

# ---------------------------------------------------------------------------
# Widget defaults
# ---------------------------------------------------------------------------
widget_defaults = dict(
    font="sans-serif",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# ---------------------------------------------------------------------------
# Bottom taskbar — Windows 10 style
# ---------------------------------------------------------------------------
screens = [
    Screen(
        bottom=bar.Bar(
            [
                # "Start" button — launches rofi
                widget.TextBox(
                    text=" Start ",
                    font="sans-serif",
                    fontsize=12,
                    foreground="#ffffff",
                    background="#2c2c2c",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                    padding=8,
                ),

                # Taskbar buttons — one per open window (Windows 10 style)
                widget.TaskList(
                    borderwidth=0,
                    icon_size=0,
                    padding=5,
                    spacing=1,
                    txt_active="#ffffff",
                    txt_normal="#888888",
                    txt_minimized="#888888",
                    background="#2c2c2c",
                    foreground="#ffffff",
                ),

                # System tray (network, volume, battery, etc.)
                widget.Systray(background="#2c2c2c", padding=5),

                # Clock
                widget.Clock(
                    format="%Y-%m-%d %H:%M",
                    foreground="#ffffff",
                    background="#2c2c2c",
                    padding=10,
                ),
            ],
            size=30,            # bar height in pixels
            background="#2c2c2c",
            opacity=1.0,
        ),
    ),
]

# ---------------------------------------------------------------------------
# Startup hook
# ---------------------------------------------------------------------------
@hook.subscribe.startup
def startup():
    wallpaper = os.path.expanduser("~/Pictures/Wallpapers/nauro.jpg")
    subprocess.Popen(["feh", "--bg-fill", wallpaper])

    subprocess.Popen(["konsole"])
