import time
import random
import pyautogui

print("Getting the first position in your bag.")
time.sleep(5)
positionX, positionY = pyautogui.position()
print("Got it.")

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Make sure to position your mouse on bank you are using.")
time.sleep(3)
print("Starting in:")
for x in range(5, 0, -1):
    print(str(x) + "...")
    time.sleep(1)

# This will be the position that continually clicks to cut wood
bankX, bankY = pyautogui.position()
print("Got position of the bank.")
print("Make sure that the bow string is one space to the right of the bows in the bank.")
time.sleep(1)
print("Now getting location of string in the bank in 5 seconds.")
time.sleep(5)
stringX, stringY = pyautogui.position()
woodX = stringX + 40
woodY = stringY
print("Got it!")
print("Starting now.")
time.sleep(1)
pyautogui.press('escape')
time.sleep(1)

for x in range(150):
    # stringing action
    pyautogui.click(positionX, positionY)
    time.sleep(random.random() + 1)
    pyautogui.moveTo(positionX, positionY + 150)
    time.sleep(random.random() * 1)
    pyautogui.click()
    time.sleep(random.random() + 2)
    pyautogui.press('space')
    time.sleep(20)

    # banking action
    pyautogui.moveTo(bankX, bankY)
    time.sleep(1)
    pyautogui.click()
    time.sleep(random.random() + 2)
    pyautogui.click(positionX, positionY)
    time.sleep(random.random() + 1)

    # withdrawing action
    pyautogui.rightClick(stringX, stringY)
    time.sleep(random.random() + 0.5)
    pyautogui.move(0, 85)
    time.sleep(random.random() * 1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(woodX, woodY)
    time.sleep(random.random() + 1)
    pyautogui.press('escape')
    time.sleep(random.random() + 1)


