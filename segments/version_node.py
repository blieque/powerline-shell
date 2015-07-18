import subprocess
import re

def add_node_version_segment():

    # run node, decode output bytestring as unicode, strip trailing whitespace
    output_node = subprocess.check_output(['node', '-v']) \
                 .decode('utf8') \
                 .rstrip()

    # extract just the version number
    match = re.search('v([0-9]+\.[0-9]+\.[0-9]+)', output_node)
    version = match.group(1)

    powerline.append(version, 22, 70)

add_node_version_segment()
