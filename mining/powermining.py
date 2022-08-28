import pyautogui
import random
import time
import threading
from pynput.keyboard import Listener, KeyCode, Controller

start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class Mining(threading.Thread):
    def __init__(self):
        super(Mining, self).__init__()
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
        print("Now getting position of the left rock...")
        time.sleep(3)
        leftRockX, leftRockY = pyautogui.position()
        print("Got it!")
        time.sleep(0.5)
        print("Now getting position of the middle rock...")
        time.sleep(3)
        midRockX, midRockY = pyautogui.position()
        print("Got it!")
        time.sleep(0.5)
        print("Now getting position of the right rock...")
        time.sleep(3)
        rightRockX, rightRockY = pyautogui.position()
        print("Got it! Press 's' to start powermining.")
        time.sleep(2)
        while self.program_run:
            while self.running:
                for x in range(9):
                    pyautogui.moveTo(leftRockX + random.random(), leftRockY + random.random())
                    time.sleep(0.25)
                    pyautogui.click()
                    time.sleep(random.random() + 1.25)
                    pyautogui.moveTo(midRockX + random.random(), midRockY + random.random())
                    time.sleep(0.25)
                    pyautogui.click()
                    time.sleep(random.random() + 1.25)
                    pyautogui.moveTo(rightRockX + random.random(), rightRockY + random.random())
                    time.sleep(0.25)
                    pyautogui.click()
                    time.sleep(random.random() + 1.25)

                ores = list(pyautogui.locateAllOnScreen('../mining/iron_ore.png'))
                for x in range(len(ores)):
                    oreX, oreY = pyautogui.center(ores[x])
                    pyautogui.keyDown('shift')
                    pyautogui.click((oreX + random.random()) / 2, (oreY + random.random()) / 2)
                    time.sleep(0.5)
                    pyautogui.keyUp('shift')
            time.sleep(0.1)

keyboard = Controller()
thread = Mining()
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






