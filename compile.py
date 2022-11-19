#!/usr/bin/env python3.7
from os import system

name = "pbrain-gomoku-ai"

system("pip install pyinstaller")
system("pyinstaller %s --onefile --name %s.exe" % (name, name))
system("cp ./dist/%s.exe ." % name)
