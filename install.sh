#!/bin/zsh
git clone https://github.com/ozrendev/osx-send-hotkey
cd osx-send-hotkey
python3 -m venv venv
source venv/bin/activate
pip install datetime

# Pynput latest version fixed for Python 3.13
git clone -b fixup/listener-thread-handle https://github.com/moses-palmer/pynput
cd pynput
pip install .
cd ..

python3 sendHotkey.py
