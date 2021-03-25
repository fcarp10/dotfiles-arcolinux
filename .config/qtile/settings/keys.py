# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        # ------------ Window Configs ------------
        # Switch between windows in current stack pane
        ([mod], "k", lazy.layout.down()),
        ([mod], "j", lazy.layout.up()),
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        # Change window sizes (MonadTall)
        ([mod, "shift"], "h", lazy.layout.grow()),
        ([mod, "shift"], "j", lazy.layout.shrink()),
        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Move windows up or down in current stack
        ([mod, "shift"], "k", lazy.layout.shuffle_down()),
        ([mod, "shift"], "j", lazy.layout.shuffle_up()),
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        # Kill window
        ([mod], "w", lazy.window.kill()),
        # Switch focus of monitors
        ([mod], "period", lazy.next_screen()),
        ([mod], "comma", lazy.prev_screen()),
        # Restart Qtile
        ([mod, "shift"], "r", lazy.restart()),
        ([mod, "shift"], "q", lazy.shutdown()),
        # ------------ App Configs ------------
        # Menu
        ([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '")),
        # Browser
        ([mod], "b", lazy.spawn("firefox")),
        # File Explorer
        ([mod], "f", lazy.spawn("thunar")),
        # Terminal
        ([mod], "Return", lazy.spawn("alacritty")),
        # editor gui
        ([mod], "e", lazy.spawn("vscodium")),
        # mail
        ([mod], "a", lazy.spawn("thunderbird")),
        # chat
        ([mod], "c", lazy.spawn("slack")),
        # arcolinux-logout
        ([mod], "x", lazy.spawn("arcolinux-logout")),
        # Screenshot
        # ([mod], "s", lazy.spawn("scrot")),
        # ------------ Hardware Configs ------------
        # Volume
        (
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        ),
        (
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        ),
        ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        # Brightness
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ]
]
