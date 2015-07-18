import os

def add_root_indicator_segment():

    root_indicator = '$'
    if os.getuid() == 0:
        root_indicator = '#'

    bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG

    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG

    powerline.append(root_indicator, fg, bg)

add_root_indicator_segment()
