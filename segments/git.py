import re
import subprocess

def get_current_fs():

    try:
        process = subprocess.Popen(
            ['stat', '-f', '-c', '%T', '.'],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        out, err = process.communicate()

        if out is not '':
            return out.strip()
        else:
            raise 'no valid output'

    except Exception, e:
        warn('could not determine local filesystem: ' + e.message)
        return None

def get_git_status():

    '''
    repository_state
        0: changes made, not all staged for commit, untracked files
        1: changes made, not all staged for commit
        2: changes made, all staged for commit
        3: no changes made, all committed
    '''
    repository_state = 3

    origin_position = ''
    output = subprocess.Popen(
        ['git', 'status', '--ignore-submodules'],
        env = { 'LANG': 'C', 'HOME': os.getenv('HOME')},
        stdout = subprocess.PIPE
    ).communicate()[0]

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

    if output.find('Untracked files') >= 0:
        repository_state = 0

    elif output.find('Changes not staged for commit') >= 0:
        repository_state = 1

    elif output.find('Changes to be committed') >= 0:
        repository_state = 2

    return repository_state, origin_position


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

    fs = get_current_fs()

    if not re.match('^nfs', fs):

        repository_state, origin_position = get_git_status()

        branch += origin_position
        if repository_state == 0:
            branch += ' +'

        bg = Color.REPO_CLEAN_BG
        fg = Color.REPO_CLEAN_FG

        if repository_state == 0 or repository_state == 1:
            bg = Color.REPO_DIRTY_BG
            fg = Color.REPO_DIRTY_FG

        elif repository_state == 2:
            bg = Color.REPO_STAGED_BG
            fg = Color.REPO_STAGED_FG

    else:
        bg = Color.REPO_UNKNOWN_BG
        fg = Color.REPO_UNKNOWN_FG
        branch += '(nfs)'

    powerline.append(branch, fg, bg)

try:
    add_git_segment()
except OSError:
    pass
except subprocess.CalledProcessError:
    pass
