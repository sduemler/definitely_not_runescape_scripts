import time
import random
import pyautogui

print("Start with your character in front of the edgeville furnace.")
time.sleep(1)

print("Place your cursor over the bank booth")
time.sleep(10)
bankX, bankY = pyautogui.position()

print("Place your cursor on the steel bars in your bank")
time.sleep(3)
steelX, steelY = pyautogui.position()

print("Place your cursor over the furnace")
time.sleep(3)
furnaceX, furnaceY = pyautogui.position()

print("Starting now!")

loops = 230

for x in range(loops):
  pyautogui.moveTo(furnaceX, furnaceY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to furnace
  time.sleep(6)

  pyautogui.press("space")

  # Smelting
  time.sleep(80)

  pyautogui.moveTo(bankX, bankY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to bank
  time.sleep(6)

  pyautogui.moveTo(steelX, steelY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(1)
  pyautogui.press("esc")
  time.sleep(1)





