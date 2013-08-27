"""Clone all git repositories in git.txt."""

import os
import sys
import re

DIR = '../'
if len(sys.argv) > 1:
    dirs = sys.argv[1:]
else:
    dirs = sorted(os.listdir(DIR))
for dir in dirs:
    if os.path.exists(os.path.join(DIR, dir, '.git')):
        print("Updating {dir}...".format(dir=dir))
        os.chdir(os.path.join(DIR, dir))
        os.system("git pull")
print("Done!")
