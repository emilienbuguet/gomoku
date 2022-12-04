#!/usr/bin/env python3
from os import system

NAME = "pbrain-gomoku-ai"

system(f"pyinstaller {NAME} --onefile --name {NAME}.exe")
system(f"cp ./dist/{NAME}.exe .")
