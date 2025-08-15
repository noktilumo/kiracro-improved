from time import sleep
from pynput import mouse, keyboard
import os
import platform

mouse_controller = mouse.Controller()

hold = False
can_run = True
running = False
keybind = 'q'


def clear_terminal():
    print("\033[2J\033[H", end="")  # Clears screen and moves cursor to top-left


def print_status():
    global running, keybind, hold
    clear_terminal()
    print(f"[FLAGS]\nholdable {hold}\nkeybind {keybind}")
    print(f"[STATES]\nrunning {running}")

def macro():
    mouse_controller.scroll(0, 1)
    sleep(0.01)

    mouse_controller.scroll(0, -1)
    sleep(0.01)

def on_press(key):
    global running, can_run, hold, keybind

    if key == keyboard.Key.esc:
        print("Pressed esc, exiting...")
        can_run = not can_run

    try:
        if key.char == keybind:
            if hold:
                running = True
                return
            else:
                running = not running

    except Exception:
        pass

def on_release(key):
    global running
    try:
        if key.char == keybind:
            if hold:
                running = False
    except Exception:
        pass

def run(holdable: bool):
    global hold
    hold = holdable
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        while can_run:
            print_status()
            if running:
                macro()
            sleep(0.1)
            
