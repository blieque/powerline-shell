import subprocess
import re

def add_python_version_segment():

    # run python, decode output bytestring as unicode, strip trailing
    # whitespace
    output_python = subprocess.check_output(['python3', '--version']) \
                 .decode('utf8') \
                 .rstrip()

    # extract just the version number
    match = re.search('Python ([0-9]+\.[0-9]+\.[0-9]+)', output_python)
    version = match.group(1)

    powerline.append(version, 117, 24)

add_python_version_segment()
