import time
import random
import pyautogui

print("Place your cursor over the cooking range..")
time.sleep(3)
rangeX, rangeY = pyautogui.position()
print("Got it.")

# This will be the position that continually clicks to cut wood
print("Place your cursor over the bank chest.")
time.sleep(3)
bankX, bankY = pyautogui.position()
print("Got position of the bank.")

print("Now getting location of the first fish in your bank.")
time.sleep(3)
fishX, fishY = pyautogui.position()
print("Got it!")

print("Now place your cursor on the deposit all button in your bank.")
time.sleep(3)
depositX, depositY = pyautogui.position();

print("Starting now.")
time.sleep(1)
pyautogui.press('escape')
time.sleep(1)

for x in range(117):
    # stringing action
    pyautogui.moveTo(rangeX, rangeY)
    time.sleep(random.random() + 0.5)
    pyautogui.click()
    time.sleep(random.random() + 1)
    pyautogui.press('space')
    time.sleep(70)

    # banking action
    pyautogui.moveTo(bankX, bankY)
    time.sleep(1)
    pyautogui.click()
    time.sleep(random.random() + 2)
    pyautogui.click(depositX, depositY)
    time.sleep(random.random() + 1)

    # withdrawing action
    pyautogui.moveTo(fishX, fishY)
    time.sleep(random.random() + 0.5)
    pyautogui.click()
    time.sleep(1)
    time.sleep(random.random() + 1)
    pyautogui.press('escape')
    time.sleep(random.random() + 1)


