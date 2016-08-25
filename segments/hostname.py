from socket import gethostname

def add_hostname_segment():
    if powerline.args.colorize_hostname:
        from lib.color_compliment import stringToHashToColorAndOpposite
        from lib.colortrans import rgb2short
        hostname = gethostname()
        FG, BG = stringToHashToColorAndOpposite(hostname)
        FG, BG = (rgb2short(*color) for color in [FG, BG])
        host_prompt = hostname.split('.')[0]

        powerline.append(host_prompt, FG, BG)
    else:
        hostname_full = gethostname()
        if powerline.args.full_hostname:
            host_prompt = hostname_full
        else:
            host_prompt = hostname_full.split('.')[0]

        powerline.append(host_prompt, Color.HOSTNAME_FG, Color.HOSTNAME_BG)

add_hostname_segment()
