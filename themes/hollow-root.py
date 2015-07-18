"""

Hollow Theme (root)
Blieque Mariguan (@blieque, GitHub and Twitter)

For use with powerline-shell (milkbikis/powerline-shell).
MIT licensed.

"""

class Color(DefaultColor):

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 67        # low-saturation blurple
    HOME_FG = 230       # cream
    PATH_BG = 0         # hex colour #002b36 (solarised base03)
    PATH_FG = 66        # low-saturation turquoise
    CWD_FG = 251        # light grey
    SEPARATOR_FG = 66   # low-saturation turquoise

    READONLY_BG = 124   # strong red
    READONLY_FG = 230   # cream

    SSH_BG = 56         # blue-ish purple
    SSH_FG = 230        # cream

    REPO_CLEAN_BG = 61  # lilac-ish
    REPO_CLEAN_FG = 230 # cream
    REPO_DIRTY_BG = 125 # hot pink-ish purple
    REPO_DIRTY_FG = 230 # cream

    CMD_PASSED_BG = 234 # dark grey
    CMD_PASSED_FG = 251 # light-ish grey
    CMD_FAILED_BG = 197 # pink
    CMD_FAILED_FG = 230 # cream
