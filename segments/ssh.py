import os

def add_ssh_segment():

    if os.getenv('SSH_CLIENT'):
        powerline.append(powerline.network, Color.SSH_FG, Color.SSH_BG)

add_ssh_segment()
