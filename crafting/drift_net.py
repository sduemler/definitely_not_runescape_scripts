import time
import pyautogui

print("Start with your character in front of the loom.")
time.sleep(1)

print("Place your cursor over the bank chest")
time.sleep(10)
bankX, bankY = pyautogui.position()

print("Place your cursor on the jute fibre in your bank")
time.sleep(3)
juteX, juteY = pyautogui.position()

print("Now getting the deposit button.")
time.sleep(3)
depositX, depositY = pyautogui.position()

print("Place your cursor over the loom")
time.sleep(3)
loomX, loomY = pyautogui.position()

print("Starting now!")

loops = 450

for x in range(loops):
  pyautogui.moveTo(loomX, loomY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to furnace
  time.sleep(8)

  pyautogui.press("space")

  # Looming
  time.sleep(27)

  pyautogui.moveTo(bankX, bankY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to bank
  time.sleep(8)

  pyautogui.moveTo(depositX, depositY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(1)

  pyautogui.moveTo(juteX, juteY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(1)
  pyautogui.press("esc")
  time.sleep(1)