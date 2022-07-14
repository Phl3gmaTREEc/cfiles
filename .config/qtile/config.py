# Default Qtile text
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

# Author of changes to default config: Phl3gmaTREEc

# Basic config
import os
import re
import socket
import subprocess
from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List

mod = "mod4"
terminal = "kitty"
browser = "firefox"
guifile = "thunar"

# Keys
keys = [
    # Switch focus between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Switch focus between monitors                                                                                                 
    # To specific monitor                                                                                                      
    # Key([mod], "e",                                                                                                          
    #    lazy.to_screen(0),                                                                                                    
    #    desc="Keyboard focus to monitor 0"                                                                                    
    #    ),                                                                                                                    
    # To next/previous monitor                                                                                                 
    Key([mod, "mod1"], "l",                                                                                                     
        lazy.next_screen(),                                                                                                   
        desc='Move focus to next monitor'                                                                                     
        ),                                                                                                                    
    Key([mod, "mod1"], "h",                                                                                                      
        lazy.prev_screen(),                                                                                                   
        desc='Move focus to prev monitor'                                                                                     
        ),
    # Move windows between left/right columns or move up/down in current stack.
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
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",),
    # Kill focused window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # Toggle WidgetBox widget
    Key([mod], "t", lazy.widget["widgetbox"].toggle(), desc="Toggle WidgetBox"),
    # Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn rofi"),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window"), desc="Spawn rofi window"),
    Key([mod], "w", lazy.spawn("/home/ptc/.config/rofi/powermenu.sh"), desc="Spawn rofi shutdown script"),
    # Launch Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn(guifile), desc="Launch gui file browser"),
    #Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using prompt widget"),
    # Keyboard Layouts
    Key(["mod1"], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Switch to next keyboard layout"),
    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    # Redshift
    KeyChord([mod], "n", [
        Key([], "n", lazy.spawn("redshift -P -O 4500 -b 0.8"),
            desc="use redshift to toggle my config on night lilght"
            ),
        Key([], "d", lazy.spawn("redshift -x"),
            desc="use redshift to goggle my config on normal light"
            )
        ]
        ),
    # Screen Layouts
    KeyChord([mod], "m", [
        Key([], "a", lazy.spawn("/home/ptc/.screenlayout/screen_layout_def.sh"),
            desc="base screen layout"
            ),
        Key([], "s", lazy.spawn("/home/ptc/.screenlayout/screen_layout_sep.sh"),
            desc="separated screen layout"
            ),
        Key([], "d", lazy.spawn("/home/ptc/.screenlayout/screen_layout_r1.sh"),
            desc="repair screen layout"
            ),
        Key([], "f", lazy.spawn("/home/ptc/.screenlayout/screen_layout_r2.sh"),
            desc="repair screen layout"
            ),
        ],
        mode="ScreenLayout"
        ),
    # Flameshot
    KeyChord([mod], "c", [
        Key([], "l", lazy.spawn("flameshot launcher"),
            desc="flameshot launcher"
            ),
        Key([], "g", lazy.spawn("flameshot gui"),
            desc="flameshot gui"
            ),
        Key([], "f", lazy.spawn("flameshot full"),
            desc="flameshot entire desktop"
            ),
        Key([], "s", lazy.spawn("flameshot screen --region 2560x1080+0-379"),
            desc="flameshot single screen"
            ),
        ]
        ),
]

# Groups
# Groups definition
groups = [Group(name="a", label='A', layout='monadtall'),
          Group(name="s", label='S', layout='monadtall'),
          Group(name="d", label='D', layout='monadtall'),
          Group(name="f", label='F', layout='monadtall'),
          Group(name="u", label='U', layout='monadtall'),
          Group(name="i", label='I', layout='verticaltile'),
          Group(name="o", label='O', layout='verticaltile'),
          Group(name="p", label='P', layout='verticaltile')]
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
            # Editing ...(i.name, switch_group=True)... also changes screen to that group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="Switch focused window to group {}".format(i.name),
            ),
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
          ["#f1fa8c", "#f1fa8c"]] # 11 - Yellow

# Layouts
# Layouts theme
layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[4],
                "border_normal": colors[1]
                }
# Layouts definition
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

# Widgets
# Widgets defaults
widget_defaults = dict(
    background=colors[0],
    font="JetBrainsMono Nerd Font Bold",
    fontsize=14,
    foreground=colors[3],
    padding=3,
)
extension_defaults = widget_defaults.copy()
## Widget list
def get_widgets(primary=False, secondary=False):
    widgets = [
## "start" button
        widget.TextBox(
            background=colors[0],
            fontsize=20,
            foreground=colors[9],
            mouse_callbacks= {
                'Button1':
                lambda: qtile.cmd_spawn("rofi -show run")
            },
            padding=10,
            text='\uE606',
            ),
## Sep
        widget.Sep(
            foreground=colors[3],
            linewidth=2,
            size_percent=75,
            ),
## Group Box
        widget.GroupBox(
            active=colors[6],
            background=colors[0],
            borderwidth=2,
            disable_drag=True,
            highlight_color=colors[0],
            highlight_method="line",
            inactive=colors[2],
            other_current_screen_border=colors[7],
            other_screen_border=colors[7],
            padding=2,
            this_current_screen_border=colors[5],
            this_screen_border=colors[8],
            urgent_alert_border=colors[10],
            urgent_alert_method='border',
            use_mouse_wheel=False,
            ),
## Sep
        widget.Sep(
            foreground=colors[3],
            size_percent=75,
            linewidth=2,
            ),
## Current Layout
        widget.CurrentLayoutIcon(
            background=colors[0],
            scale=0.7,
            ),
## Sep
        widget.Sep(
            foreground=colors[3],
            linewidth=2,
            size_percent=75,
            ),
## Window Name & Chord
        widget.WindowName(
            foreground=colors[3],
            ),
        widget.Chord(
            foreground=colors[4],
            ),
## Sep
        widget.Sep(
            foreground=colors[3],
            linewidth=2,
            size_percent=75,
            ),
## Keyboard Layout
        widget.KeyboardLayout(
            background=colors[0],
            configured_keyboards=['cz','us'],
            foreground=colors[11],
            padding=5,
            ),
## Sep
        widget.Sep(
            foreground=colors[3],
            linewidth=2,
            size_percent=75,
            ),
## Power button
        widget.TextBox(
            background=colors[0],
            foreground=colors[10],
            mouse_callbacks= {
                'Button1':
                lambda: qtile.cmd_spawn(os.path.expanduser('/home/ptc/.config/rofi/powermenu.sh'))
            },
            padding=10,
            text='\uF011',
            ),
#### Inactive
#        widget.TextBox(
#            text='\uE0B0',
#            padding=0,
#            fontsize=25,
#            foreground=colors[0],
#            background=colors[4],
#            ),
#        widget.TextBox(    
#            text='\uE0B2',
#            padding=0,
#            fontsize=25,
#            foreground=colors[4],
#            background=colors[0],
#            ),
#        widget.TextBox(    
#            text='\uE0B3',
#            padding=0,
#            fontsize=25,
#            foreground=colors[4],
#            ),
#        widget.Prompt(),
#        widget.CapsNumLockIndicator(),
#        widget.CheckUpdates(),
#        widget.GenPollText(
#           update_interval=1,
#           func=lambda: subprocess.check_output(
#                   "/home/ptc/.config/qtile/scripts/volume.sh").decode().strip(),
#           mouse_callbacks = {
#                   'Button1': lazy.spawn("pavucontrol -t 3"),
#                   'Button3': lazy.spawn("pamixer -t")
#                   }
#           ),
        ]
## Inserting widgets per screen
    if primary:
## Sep
        widgets.insert(8,
            widget.Sep(
                foreground=colors[3],
                linewidth=2,
                size_percent=75,
            ),
        )
## Widget box - systray
        widgets.insert(9,
            widget.WidgetBox(widgets=[
                widget.Systray(
                    background=colors[0],
                ),
                widget.Sep(
                    foreground=colors[3],
                    linewidth=2,
                    size_percent=75,
                ),
            ],
                close_button_location="right",
                foreground=colors[6],
            ),
        )
## Sep
        widgets.insert(10,
            widget.Sep(
                foreground=colors[3],
                linewidth=2,
                size_percent=75,
            ),
        )
## Time and date
        widgets.insert(11,
            widget.Clock(
                background=colors[0],
                foreground=colors[9],
                format="%Y-%m-%d %a %H:%M",
            ),
        )
    if secondary:
## Sep
        widgets.insert(8,
            widget.Sep(
                foreground=colors[3],
                linewidth=2,
                size_percent=75,
            ),
        )
## Time and date
        widgets.insert(9,
            widget.Clock(
                background=colors[0],
                foreground=colors[9],
                format="%y-%m-%d %H:%M",
            ),
        )
    return widgets

## Old way of doing widgets per screen
# Widget filtered lists
#def init_widgets_screen1():
#    widgets_screen1 = init_widgets_list()
#    del widgets_screen1[11]
#    return widgets_screen1
#
#def init_widgets_screen2():
#    widgets_screen2 = init_widgets_list()
#    del widgets_screen2[8:11]
#    return widgets_screen2

# Screens
screens = [
    Screen(
        bottom=bar.Bar(
            get_widgets(primary=True),
            size=24),
        ),
    Screen(
        bottom=bar.Bar(
            get_widgets(secondary=True),
            size=24),
        )
]

# Floating layout
# FLoating layout settings
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

# Additional config
# Simple line configs
auto_fullscreen = True
auto_minimize = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
wl_input_rules = None
wmname = "LG3D"

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
