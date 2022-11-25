#!/usr/bin/env python3.7
from os import system

NAME = "pbrain-gomoku-ai"

system("pip install pyinstaller")
system(f"pyinstaller {NAME} --onefile --name {NAME}.exe")
system(f"cp ./dist/{NAME}.exe .")
