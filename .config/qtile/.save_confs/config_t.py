# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List

mod = "mod4"
terminal = guess_terminal("kitty")

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Switch focus of monitors
    # To specific monitor
    # Key([mod], "e",
    #    lazy.to_screen(0),
    #    desc="Keyboard focus to monitor 0"
    #    ),
    # To next/previous monitor
    # Key([mod], "period",
    #    lazy.next_screen(),
    #    desc='Move focus to next monitor'
    #    ),
    # Key([mod], "comma",
    #    lazy.prev_screen(),
    #    desc='Move focus to prev monitor'
    #    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    # Launch Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn rofi"),
    Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using prompt widget"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    # Kill focused window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    
    # Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Groups
# Groups definition
groups = [Group("a", layout='monadtall'),
          Group("s", layout='monadtall'),
          Group("d", layout='monadtall'),
          Group("f", layout='monadtall'),
          Group("u", layout='monadtall'),
          Group("i", layout='VerticalTile'),
          Group("o", layout='VerticalTile'),
          Group("p", layout='VerticalTile')]

# Groups keys
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Colors
colors = [["#282a36", "#282a36"], # 0 - Background
          ["#44475a", "#44475a"],  # 1 - Current line
          ["#44475a", "#44475a"],  # 2 - Selection
          ["#f8f8f2", "#f8f8f2"],  # 3 - Foreground
          ["#6272a4", "#6272a4"],  # 4 - Comment
          ["#8be9fd", "#8be9fd"],  # 5 - Cyan
          ["#50fa7b", "#50fa7b"],  # 6 - Green 
          ["#ffb86c", "#ffb86c"],  # 7 -Orange
          ["#ff79c6", "#ff79c6"],  # 8 - Pink 
          ["#bd93f9", "#bd93f9"],  # 9 - Purple
          ["#ff5555", "#ff5555"],  # 10 - Red
          ["#f1fa8c", "#f1fa8c"],] # 11 - Yellow

# Layouts
# Layouts theme
layout theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[9]
                "border_normal": colors[4]
                }

# Layouts definition
layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

# Widgets
# Widgets defaults
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    background=colors[4]
)
extension_defaults = widget_defaults.copy()

# Widget list
def init_widgets_list():
    widgets_list = [
            widget.Image(
                filename = "~/.config/qtile/eos-c.png",
                scale = "False",
                ),
            widget.GroupBox(),
            widget.CurrentLayoutIcon(),
            widget.CurrentLayout(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
            widget.Systray(),
            widget.Clock(format="%Y-%m-%d %a %H:%M"),
        ]
    return widget_list

# Widget filtered lists
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[8]
    return widgets_screen2

# Screens
screens = [
    Screen(
        bottom=bar.Bar(widgets=init_widgets_screen1(), size=24
        ),
    Screen(
        bottom=bar.Bar(widgets=init_widgets_screen2(), size=24
        ),    
]

# FLoating layout settings
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Floating rules
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# Simple line configs
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
