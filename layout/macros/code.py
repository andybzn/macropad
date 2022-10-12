# SPDX-FileCopyrightText: 2022 Andy Baizon
# SPDX-License-Identifier: MIT
# Hotkeys for VSCode

from adafruit_hid.keycode import Keycode  # import keycodes

app = {
    "name": "Visual Studio Code",  # application
    "macros": [  # macro list
        # row one
        (0x000010, "Zen", [Keycode.CONTROL, "k", "z"]),  # toggle zen mode
        (0x000010, "Palette", [Keycode.CONTROL, Keycode.SHIFT, "p"]),  # open command palette
        (0x000010, "Term", [Keycode.CONTROL, Keycode.SHIFT, "\'"]),  # launch a new terminal instance
        # row two
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        # row three
        (0x000040, "Fmt", [Keycode.SHIFT, Keycode.ALT, "f"]),  # format document
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        # row four
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        # click pot
        (0x000000, "", [Keycode.ALT, "F4"]),  # nope out
    ],
}
