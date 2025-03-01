import time
import random
import pyautogui

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Make sure to position your mouse on bank you are using.")
time.sleep(3)
print("Starting in:")
for x in range(3, 0, -1):
    print(str(x) + "...")
    time.sleep(1)

# This will be the position that continually clicks to cut wood
bankX, bankY = pyautogui.position()
print("Got position of the bank.")
print("Now getting location of wood in the bank in 5 seconds.")
time.sleep(5)
woodX, woodY = pyautogui.position()
print("Got it!")
print("Starting now.")
time.sleep(1)
pyautogui.press('escape')
time.sleep(1)

# Locate where the knife is in the inventory
knifeX, knifeY = pyautogui.locateCenterOnScreen('fletching/runescape_knife.png', grayscale=True, confidence=0.8)

for x in range(134):
    pyautogui.click(knifeX / 2, knifeY / 2)
    time.sleep(random.random() + 1)
    pyautogui.click((knifeX / 2) + 40, knifeY / 2)
    time.sleep(random.random() + 2)
    pyautogui.press('space')
    time.sleep(50)

    pyautogui.moveTo(bankX, bankY)
    time.sleep(1)
    pyautogui.click()
    time.sleep(random.random() + 2)
    pyautogui.click((knifeX / 2) + 40, knifeY / 2)
    time.sleep(random.random() + 1)
    pyautogui.click(woodX, woodY)
    time.sleep(random.random() + 1)
    pyautogui.press('escape')
    time.sleep(random.random() + 1)


