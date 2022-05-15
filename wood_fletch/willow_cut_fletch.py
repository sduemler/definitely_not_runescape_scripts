import time
import random
import pyautogui

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Make sure to position your mouse on the tree you want to cut!")
time.sleep(3)
print("Starting in:")
for x in range(5, 0, -1):
    print(str(x) + "...")
    time.sleep(1)
print("Starting now!")

# This will be the position that continually clicks to cut wood
clickX, clickY = pyautogui.position()


for x in range(100):
    logs = list(pyautogui.locateAllOnScreen('wood_fletch/runescape_willow_log.png', grayscale=True))
    if (len(logs) == 21):
        # Locate where the knife is in the inventory
        knifeX, knifeY = pyautogui.locateCenterOnScreen('wood_fletch/runescape_knife.png', grayscale=True)

        #Locate where a log is in the inventory
        logX, logY = pyautogui.locateCenterOnScreen('wood_fletch/runescape_willow_log.png', grayscale=True)

        pyautogui.click(knifeX / 2, knifeY / 2)
        time.sleep(random.random() + 1)
        pyautogui.click(logX / 2, logY / 2)
        time.sleep(random.random() + 2)
        pyautogui.press('space')
        time.sleep(40)
    else:
        pyautogui.click(clickX, clickY)
        time.sleep(random.random() + 15)
    print(str(100 - x) + " runs left!")

