import subprocess
import re

def add_php_version_segment():

    # run php, decode output bytestring as unicode, strip trailing whitespace
    output_php = subprocess.check_output(['php', '-v']) \
                 .decode('utf8') \
                 .rstrip()

    # extract just the version number
    match = re.search('PHP ([0-9]+\.[0-9]+\.[0-9]+)', output_php)
    version = match.group(1)

    powerline.append(version, 237, 104)

add_php_version_segment()
