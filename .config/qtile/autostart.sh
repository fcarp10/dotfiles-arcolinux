#!/bin/sh

# cbatticon -u 5 & # systray battery icon
nm-applet & # systray network
numlockx on &
pamac-tray &
syncthing &
picom -b --config  $HOME/.config/qtile/picom.conf
xrandr --output DP1-8 --primary --mode 1920x1200 --output HDMI3 --mode 1920x1200 --left-of DP1-8