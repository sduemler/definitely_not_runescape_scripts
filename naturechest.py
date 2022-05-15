import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 15
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
        runs = 0
        while self.program_run:
            while self.running and runs <= 1500:
                mouse.click(Button.right)
                mouse.move(0, 40)
                time.sleep(1)
                mouse.click(self.button)
                mouse.move(0, -40)
                time.sleep(self.delay)
                runs += 1
                if runs == 1500:
                    print(runs)
            time.sleep(0.1)

mouse = Controller()
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