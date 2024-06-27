import time
import random
import pyautogui
import threading
from pynput.keyboard import Listener, KeyCode, Controller

print("Place your cursor over the firstPosition.")
time.sleep(3)
firstX, firstY = pyautogui.position()

print("Now place your cursor 1 square NW diagonal from you,")
time.sleep(3)
secondX, secondY = pyautogui.position()

print("Ready!")

d = abs(secondX - firstX)

# print("Now run 3 tiles west, and place your cursor on the tile it began on.")
# time.sleep(5)
# returnX, returnY = pyautogui.position()

# print("Now ruin back to your original position and press the s key when ready to start.")

# start
# 1 left
# stay


# stay
# up 1 right 1
# 2 right 2 down
# 1 left 1 down
# stay
# 1 left 1 down
# 2 left 2 up
# 1 up 1 right




start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class Fishing(threading.Thread):
    def __init__(self):
        super(Fishing, self).__init__()
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
                pyautogui.moveTo(firstX, firstY)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(14.9)
                pyautogui.moveTo(secondX, secondY)
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(14.9)
                pyautogui.click()
                time.sleep(14.9)

                for x in range(150):
                    pyautogui.moveTo(secondX, secondY)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(15)
                    pyautogui.move(d, -d)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(14.4)
                    pyautogui.move(d * 2, d * 2)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(14.4)
                    pyautogui.move(-d, d)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(15)
                    pyautogui.click()
                    time.sleep(15)
                    pyautogui.move(-d, d)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(14.4)
                    pyautogui.move(-(d * 2), -(d * 2))
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(14.4)
                    pyautogui.move(d, -d)
                    time.sleep(0.1)
                    pyautogui.click()
                    time.sleep(15)


keyboard = Controller()
thread = Fishing()
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