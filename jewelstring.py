import time
import random
import pyautogui

print("Getting the spell location.")
time.sleep(5)
spellX, spellY = pyautogui.position()
print("Got it.")

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Make sure to position your mouse on bank you are using.")
time.sleep(5)
bankX, bankY = pyautogui.position()
print("Got position of the bank.")
time.sleep(1)
print("Now getting location of string in the bank in 5 seconds.")
time.sleep(5)
amuletX, amuletY = pyautogui.position()
print("Got it!")
print("Starting now.")
time.sleep(1)
pyautogui.press('escape')
time.sleep(1)

for x in range(72):
    pyautogui.click(spellX, spellY)
    time.sleep(50)
    pyautogui.moveTo(bankX, bankY)
    time.sleep(1)
    pyautogui.click()
    time.sleep(random.random() + 2)
    pyautogui.moveTo(spellX + 10, spellY + 15)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(amuletX, amuletY)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep((random.random() + 2))
    pyautogui.press('escape')
    time.sleep(2)
