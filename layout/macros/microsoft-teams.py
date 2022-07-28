# SPDX-FileCopyrightText: 2022 Andy Baizon
# SPDX-License-Identifier: MIT
# Hotkeys for MSFT Teams

from adafruit_hid.keycode import Keycode  # import keycodes

app = {
    "name": "MSFT Teams",  # application
    "macros": [  # macro list
        # row one
        (0x004000, "Activity", [Keycode.ALT, "ONE"]),  # open activity pane
        (0x004000, "Chat", [Keycode.ALT, "TWO"]),  # open chat pane
        (0x400000, "Cmd", [Keycode.ALT, "K"]),  # open command bar
        # row two
        (0x202000, "Teams", [Keycode.ALT, "THREE"]),  # open teams list pane
        (0x202000, "Cal", [Keycode.ALT, "FOUR"]),  # open calendar pane
        (0x400000, "Files", [Keycode.ALT, "FIVE"]),  # open files pane
        # row three
        (0x000040, "", [Keycode.CONTROL, ""]),
        (0x000040, "Camera", [Keycode.CONTROL, Keycode.ALT, "o"]),  # toggle camera
        (0x000040, "", [Keycode.CONTROL, ""]),
        # row four
        (0x000000, "Mute", [Keycode.CONTROL, Keycode.ALT, "n"]),  # toggle mute
        (0x800000, "Accept", [Keycode.CONTROL, Keycode.ALT, "a"]),  # accept call
        (0x101010, "Decline", [Keycode.CONTROL, Keycode.ALT, "d"]),  # decline call
        # click pot
        (0x000000, "", [Keycode.ALT, "F4"]),  # nope out
    ],
}
