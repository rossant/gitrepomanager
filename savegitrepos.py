"""Save in git.txt the name and URL of all git repositories in the $
current folder."""
import os
import sys
import re

DIR = '../'
repos = []
pattern = """[remote "origin"]\n\turl = """
dirs = os.listdir(DIR)
for dir in sorted(dirs):
    if os.path.exists(os.path.join(DIR, dir, '.git')):
        filename = os.path.join(DIR, dir, '.git', 'config')
        config = open(filename).read()
        i = config.find(pattern)
        if i:
            i = i + len(pattern)
            j = config[i:].find('\n')
            repos += [dir + " " + config[i:i + j]]
        
with open("git.txt", "w") as f:
    f.write("\n".join(repos))
