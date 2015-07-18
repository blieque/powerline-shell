import re
import subprocess

def get_git_status():

    has_pending_commits = True
    has_untracked_files = False
    origin_position = ''
    output = subprocess.Popen(['git', 'status', '--ignore-submodules'],
             env = { 'LANG': 'C', 'HOME': os.getenv('HOME')},
             stdout=subprocess.PIPE).communicate()[0]

    origin_status = \
        re.findall(r"Your branch is (ahead|behind).*?(\d+) commit", output)
    diverged_status = \
        re.findall(r"and have (\d+) and (\d+) different commit", output)

    if origin_status:

        origin_position = " %d" % int(origin_status[0][1])
        if origin_status[0][0] == 'behind':
            origin_position += u'\u21E3'
        if origin_status[0][0] == 'ahead':
            origin_position += u'\u21E1'

    if diverged_status:
        origin_position = " %d%c %d%c" % \
            (int(diverged_status[0][0]),
            u'\u21E1',
            int(diverged_status[0][1]),
            u'\u21E3')

    if output.find('nothing to commit') >= 0:
        has_pending_commits = False

    if output.find('Untracked files') >= 0:
        has_untracked_files = True

    return has_pending_commits, has_untracked_files, origin_position


def add_git_segment():

    process = subprocess.Popen(
        ['git', 'symbolic-ref', '-q', 'HEAD'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, err = process.communicate()

    if 'Not a git repo' in err:
        return

    branch = u'\ue0a0 '
    if out:
        # strip leading 'refs/heads/' and trailing newline
        branch += out[11:].rstrip()
    else:
        branch += '(detached)'

    has_pending_commits, has_untracked_files, origin_position = \
        get_git_status()

    branch += origin_position
    if has_untracked_files:
        #branch += u' \u271A' # fatter unicode plus symbol
        branch += ' +'

    bg = Color.REPO_CLEAN_BG
    fg = Color.REPO_CLEAN_FG

    if has_pending_commits:
        bg = Color.REPO_DIRTY_BG
        fg = Color.REPO_DIRTY_FG
    #    branch += u' \u2718' # unicode 'x' shape
    #else:
    #    branch += u' \u2714' # unicode check mark/tick

    powerline.append(branch, fg, bg)

try:
    add_git_segment()
except OSError:
    pass
except subprocess.CalledProcessError:
    pass
