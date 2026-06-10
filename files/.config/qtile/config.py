"""
Qtile Configuration ??? Windows 10 Inspired Minimal Setup
========================================================

Principles:
  - No tiling: all windows float freely (like a traditional desktop).
  - Bottom taskbar with: start button, workspace list, window title,
    system tray, and clock.
  - Always-visible window borders (focused = blue, unfocused = dark).
  - rofi (Super+R / Start button) acts as the application launcher.
  - Super+Return opens a terminal (konsole by default).

Keybindings
-----------
  Super+Return    terminal
  Super+R         rofi (app launcher / start menu)
  Super+Q         close focused window
  Super+1..9      switch to workspace
  Super+Shift+1..9 move window to workspace
  Super+Shift+R   reload config
  Super+Ctrl+R    restart qtile
  Alt+Tab         cycle windows
  Alt+Shift+Tab   cycle windows (reverse)

Mouse
-----
  Super+drag       move floating window
  Super+right-drag resize floating window
  Super+middle-click bring window to front
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
    # Close focused window
    Key([mod], "q", lazy.window.kill()),
    # Reload config without restarting
    Key([mod, "shift"], "r", lazy.reload_config()),
    # Full restart
    Key([mod, "control"], "r", lazy.restart()),
    # Window cycling (Alt+Tab style)
    Key(["mod1"], "Tab", lazy.layout.next()),
    Key(["mod1", "shift"], "Tab", lazy.layout.previous()),
]

# ---------------------------------------------------------------------------
# Workspaces (up to 9, accessed via Super+[1-9])
# ---------------------------------------------------------------------------
groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

for i, group in enumerate(groups):
    key = str(i + 1)
    keys.append(Key([mod], key, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, "shift"], key, lazy.window.togroup(group.name)))

# ---------------------------------------------------------------------------
# Layouts ??? empty on purpose: no tiling, everything floats
# ---------------------------------------------------------------------------
layouts = [layout.Max()]

# Floating window appearance (borders + decorations)
floating_layout = layout.Floating(
    border_focus="#5294e2",    # focused border = blue accent
    border_normal="#2c2c2c",   # unfocused border = dark grey
    border_width=2,
    fullscreen_border_width=0,
    max_border_width=0,
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
# Bottom bar ??? Windows 10 style taskbar
# ---------------------------------------------------------------------------
screens = [
    Screen(
        bottom=bar.Bar(
            [
                # "Start" button ??? launches rofi
                widget.TextBox(
                    text=" Start ",
                    font="sans-serif",
                    fontsize=12,
                    foreground="#ffffff",
                    background="#2c2c2c",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                    padding=8,
                ),

                # Workspace switcher (like virtual desktop buttons)
                widget.GroupBox(
                    font="sans-serif",
                    fontsize=12,
                    margin_x=2,
                    margin_y=2,
                    padding_x=4,
                    padding_y=4,
                    borderwidth=0,
                    active="#ffffff",
                    inactive="#888888",
                    rounded=False,
                    highlight_color="#5294e2",
                    highlight_method="block",
                    this_current_screen_border="#5294e2",
                    this_screen_border="#444444",
                    other_current_screen_border="#5294e2",
                    other_screen_border="#444444",
                    foreground="#ffffff",
                    background="#2c2c2c",
                    disable_drag=True,
                ),

                # Title of currently focused window
                widget.WindowName(
                    font="sans-serif",
                    fontsize=12,
                    foreground="#ffffff",
                    background="#2c2c2c",
                    padding=10,
                    width=bar.CALCULATED,
                ),

                # Push everything right of the window title
                widget.Spacer(background="#2c2c2c"),

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

# ---------------------------------------------------------------------------
# Force every new window to float
# ---------------------------------------------------------------------------
@hook.subscribe.client_new
def float_all_windows(client):
    """Make every window floating ??? no tiling, ever."""
    client.floating = True
