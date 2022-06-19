#!/bin/sh

# Xrandr script
~/.screenlayout/screen_layout1.sh &

# Compositor
picom & # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Start polkit agent from GNOME
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Start apps
pasystray &
solaar --window=hide &
easyeffects --gapplication-service &
qpwgraph -m &
nm-applet &
blueman-applet &
discord --start-minimized &
steam -silent &
flameshot &
# eos-welcome &

# Backgrounds
feh --bg-fill ~/Pictures/Wallpapers/arch3.jpg
