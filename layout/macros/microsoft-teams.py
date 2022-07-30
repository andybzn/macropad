# SPDX-FileCopyrightText: 2022 Andy Baizon
# SPDX-License-Identifier: MIT
# Hotkeys for MSFT Teams

from adafruit_hid.keycode import Keycode  # import keycodes

app = {
    "name": "MSFT Teams",  # application
    "macros": [  # macro list
        # row one
        (0x004000, "Activity", [Keycode.CONTROL, "ONE"]),  # open activity pane
        (0x004000, "Chat", [Keycode.CONTROL, "TWO"]),  # open chat pane
        (0x400000, "Cmd", [Keycode.CONTROL, "/"]),  # open command bar
        # row two
        (0x202000, "Teams", [Keycode.CONTROL, "THREE"]),  # open teams list pane
        (0x202000, "Cal", [Keycode.CONTROL, "FOUR"]),  # open calendar pane
        (0x400000, "Files", [Keycode.CONTROL, "FIVE"]),  # open files pane
        # row three
        (0x000040, "Join", [Keycode.CONTROL, Keycode.SHIFT, "J"]),  # join meeting
        (0x000040, "Cam", [Keycode.CONTROL, Keycode.SHIFT, "O"]),  # toggle camera
        (0x000040, "PTT", [Keycode.CONTROL, Keycode.SPACE]), # push to talk
        # row four
        (0x004000, "Acpt", [Keycode.CONTROL, Keycode.SHIFT, "S"]),  # accept call
        (0x000000, "Mute", [Keycode.CONTROL, Keycode.SHIFT, "M"]),  # toggle mute
        (0x800000, "Dclne", [Keycode.CONTROL, Keycode.SHIFT, "D"]),  # decline call
        # click pot
        (0x000000, "", [Keycode.ALT, "F4"]),  # nope out
    ],
}
