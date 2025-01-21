import subprocess
from pynput import keyboard
from datetime import datetime

def initHotkey(keyPressed):

    applescriptCode = f"""
    try
        set hotkey to \"{keyPressed}\"
        set siteList to ("https://platform.alpha-futures.com/trade", "https://topstepx.com/trade","https://bulenox.projectx.com/trade","https://futureselite.projectx.com/trade","https://trader.tradovate.com")
        activate application "Safari"
        repeat with site in siteList 
            repeat 1 times
                try
                    tell application "Safari" to set theTab to first tab of window 1 whose URL contains site
                    tell application "Safari" to tell front window to set current tab to theTab
                    tell application "System Events"
                        delay 0.5
                        keystroke hotkey using shift down
                        delay 0.25
                    end tell
                    delay 1 
                on error
                    -- Skip URL if it's not open
                    exit repeat
                end try 
            end repeat
        end repeat
    on error errStr
        return errStr
    end try
"""

    subprocess.call(['osascript', '-e', applescriptCode])
    print(f'[{datetime.now()}] Shift+{keyPressed}')

SHIFT_J = {keyboard.Key.shift, keyboard.KeyCode(char='J')}
SHIFT_K = {keyboard.Key.shift, keyboard.KeyCode(char='K')}
SHIFT_U = {keyboard.Key.shift, keyboard.KeyCode(char='U')}
SHIFT_I = {keyboard.Key.shift, keyboard.KeyCode(char='I')}
SHIFT_P = {keyboard.Key.shift, keyboard.KeyCode(char='P')}
SHIFT_L = {keyboard.Key.shift, keyboard.KeyCode(char='L')}

current = set()

def on_press(key):

    if key in SHIFT_J:
        current.add(key)
        if all(k in current for k in SHIFT_J):
            initHotkey("J")

    elif key in SHIFT_K:
        current.add(key)
        if all(k in current for k in SHIFT_K):
            initHotkey("K")

    elif key in SHIFT_U:
        current.add(key)
        if all(k in current for k in SHIFT_U):
            initHotkey("U")

    elif key in SHIFT_I:
        current.add(key)
        if all(k in current for k in SHIFT_I):
            initHotkey("I")

    elif key in SHIFT_P:
        current.add(key)
        if all(k in current for k in SHIFT_P):
            initHotkey("P")

    elif key in SHIFT_L:
        current.add(key)
        if all(k in current for k in SHIFT_L):
            initHotkey("L")

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
