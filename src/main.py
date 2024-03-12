import time
import threading

# keyboard/os imports
import keyboard

# tray imports
import pystray
import PIL.Image


# --- THREAD 1 BLOCK ---

# START BLOCK define functions for tray
def tray_click_function():
    print("Hello world")


def tray_click_exit():
    tray_icon.stop()
# END BLOCK define functions for tray


# load icon for tray
tray_icon = PIL.Image.open("PB.png")

# create tray icon object
tray_icon = pystray.Icon("PB", tray_icon, menu=pystray.Menu(
    pystray.MenuItem("Function Test", tray_click_function),
    pystray.MenuItem("Exit", tray_click_exit)
))


ThreadTray = threading.Thread(target=tray_icon.run)
ThreadTray.start()

# --- THREAD 1 BLOCK END ---


# --- THREAD 2 BLOCK ---
# This thread is daemon, when Thread 1 ends whole program closes


def keyboard_check():

    def minimize_windows():
        keyboard.send("Windows+M")
        print("Done")

    keyboard.add_hotkey("9", minimize_windows)

    x = 0
    while True:
        time.sleep(1)
        print(x, end=" ")

        print()
        x = x + 1


ThreadKeyboard = threading.Thread(target=keyboard_check, daemon=True)
ThreadKeyboard.start()

# --- THREAD 2 BLOCK END ---
