#!/usr/bin/env python3.7
from os import system

name = "pbrain-gomoku-ai"
main = "./sources/main.py"

system("pyinstaller %s --onefile --name %s.exe" % (main, name))
system("cp ./dist/%s.exe ." % name)