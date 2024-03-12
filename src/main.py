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
# keyboard.add_hotkey("2+3", print, args=("test",))


def keyboard_check():
    x = 0

    while True:
        time.sleep(1)
        print(x, end=" ")

        if keyboard.is_pressed("2+3"):
            print("Pressed", end="")
        else:
            pass

        print()
        x = x + 1


ThreadKeyboard = threading.Thread(target=keyboard_check, daemon=True)
ThreadKeyboard.start()

# --- THREAD 2 BLOCK END ---
