"""Clone all git repositories in git.txt."""

import os
import sys
import re

gitrepos = open("git.txt").read().split("\n")

os.chdir("..")
for line in gitrepos:
    name, url = line.split(" ")
    print name
    os.system("git clone " + url)
    print
