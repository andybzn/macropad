# SPDX-FileCopyrightText: 2022 Andy Baizon
# SPDX-License-Identifier: MIT
# Hotkeys for Vim

from adafruit_hid.keycode import Keycode  # import keycodes

app = {
    "name": "Vim",  # application
    "macros": [  # macro list
        # row one
        (0x000040, ":q!", [":", "q", "!"]),  # hard quit 
        (0x000010, ":wq!", [":", "w", "q"]),  # save and quit 
        (0x000000, "dd", ["d", "d"]),  # delete line
        # row two
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        (0x000000, "", [""]),  # nothing
        # row three
        (0x000000, "", [""]),  # nothing
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
