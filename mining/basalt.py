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
        print("Now getting fourth position in bag.")
        time.sleep(3)
        bagX, bagY =  pyautogui.position()
        print("Now getting position of Snowflake...")
        time.sleep(5)
        snowflakeX, snowflakeY = pyautogui.position()
        print("Got it!")
        time.sleep(0.5)
        print("Now getting position of the stairs...")
        time.sleep(5)
        downstairsX, downstairsY = pyautogui.position()
        print("Got it! Please go down the stairs and point to the basalt.")
        time.sleep(8)
        basaltFarX, basaltFarY = pyautogui.position()
        print("Got it!")
        time.sleep(0.5)
        print("Now standing next to the basalt, hold your cursor over it again.")
        time.sleep(5)
        basaltNearX, basaltNearY = pyautogui.position()
        time.sleep(0.5)
        print("Okay last thing, now hover over the stairs going up.")
        time.sleep(3)
        upstairsX, upstairsY = pyautogui.position()
        print("Got it! Now printing money.")
        while self.program_run:
            while self.running:
                for x in range(10):
                    pyautogui.moveTo(basaltNearX + random.random(), basaltNearY + random.random())
                    time.sleep(0.25)
                    pyautogui.click()
                    time.sleep(8 + random.random())
                pyautogui.moveTo(upstairsX + random.random(), upstairsY + random.random())
                time.sleep(1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(8)
                pyautogui.moveTo(bagX, bagY)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.moveTo(snowflakeX, snowflakeY)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(5)
                pyautogui.moveTo(downstairsX + random.random(), downstairsY + random.random())
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(8)
                pyautogui.moveTo(basaltFarX, basaltFarY)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(10)
            time.sleep(1)

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






