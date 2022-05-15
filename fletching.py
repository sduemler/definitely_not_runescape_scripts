import time
import threading

import pynput.mouse
from pynput.mouse import Button
from pynput.keyboard import Listener, KeyCode, Key

delay = 1.5
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                mouse.move(40, 0)
                time.sleep(1)
                mouse.click(self.button)
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                mouse.move(-40, 0)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
thread = ClickMouse(delay, button)
thread.start()


def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
            print("Stopping.")
        else:
            thread.start_clicking()
            print("Starting...")
    elif key == exit_key:
        thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()