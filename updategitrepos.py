"""Clone all git repositories in git.txt."""

import os
import sys
import re

DIR = '../'
dirs = os.listdir(DIR)
for dir in sorted(dirs):
    if os.path.exists(os.path.join(DIR, dir, '.git')):
        print dir
        os.chdir(os.path.join(DIR, dir))
        os.system("git pull")
        print
