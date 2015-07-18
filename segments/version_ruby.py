import os
import subprocess
import re

def add_ruby_version_segment():

    # run ruby, decode output bytestring as unicode, strip trailing whitespace
    output_ruby = subprocess.check_output(['ruby', '-v']) \
                 .decode('utf8') \
                 .rstrip()

    # extract just the version number
    match = re.search('ruby ([0-9]+\.[0-9]+\.[0-9]+)', output_ruby)
    version = match.group(1)

    # something to do with gems that I didn't write
    if 'GEM_HOME' in os.environ:
        gem = os.environ['GEM_HOME'].split('@')
        if len(gem) > 1:
            version += ' ' + gem[1]

    powerline.append(version, 174, 124)

try:
    add_ruby_version_segment()
except OSError:
    pass
