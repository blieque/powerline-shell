
def add_username_segment():
    import os
    user_prompt = os.getenv('USER')

    if user_prompt == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    powerline.append(user_prompt, Color.USERNAME_FG, bgcolor)

add_username_segment()
