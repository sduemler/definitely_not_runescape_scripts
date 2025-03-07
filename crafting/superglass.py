import time
import random
import pyautogui

print("Open your spellbook and hover your mouse over the superglass make spell.")
time.sleep(3)
superglassX, superglassY = pyautogui.position()

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Make sure to position your mouse on bank you are using.")
time.sleep(3)
# This will be the position that continually clicks to cut wood
bankX, bankY = pyautogui.position()
print("Got position of the bank.")

print("Now getting location of sand in the bank in 3 seconds.")
time.sleep(3)
sandX, sandY = pyautogui.position()
seaweedX = sandX + 40
seaweedY = sandY
print("Got it!")
print("For the last thing I need the deposit button")
time.sleep(3)
depositX, depositY = pyautogui.position()
print("Starting now.")
time.sleep(1)
pyautogui.press('escape')
time.sleep(1)

for x in range(943):
    # stringing action
    pyautogui.click(superglassX, superglassY)
    time.sleep(random.random() + 2)

    # banking action
    pyautogui.moveTo(bankX, bankY)
    time.sleep(random.random() + 0.5)
    pyautogui.click()
    time.sleep(random.random() + 0.5)
    pyautogui.click(depositX, depositY)
    time.sleep(random.random() + 0.5)

    # withdrawing action
    pyautogui.click(sandX, sandY)
    time.sleep(1)
    for y in range(3):  
      pyautogui.click(seaweedX, seaweedY)
      time.sleep(random.random() + 0.5)
    pyautogui.press('escape')
    time.sleep(random.random() + 0.5)


