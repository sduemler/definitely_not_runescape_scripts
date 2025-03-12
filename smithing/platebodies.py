import time
import pyautogui

print("Start with your character in front of smithing anvil.")
time.sleep(1)

print("Place your cursor over the bank booth")
time.sleep(5)
bankX, bankY = pyautogui.position()

print("Place your cursor on the bars you want to use in your bank")
time.sleep(3)
barX, barY = pyautogui.position()

print("Now over the deposit button.")
time.sleep(3)
depositX, depositY = pyautogui.position()

print("Place your cursor over the anvil")
time.sleep(3)
anvilX, anvilY = pyautogui.position()

print("Starting now!")

loops = 200

for x in range(loops):
  pyautogui.moveTo(anvilX, anvilY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to furnace
  time.sleep(5)

  pyautogui.press("space")

  # Smelting
  time.sleep(14)

  pyautogui.moveTo(bankX, bankY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to bank
  time.sleep(5)

  pyautogui.moveTo(depositX, depositY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(0.5)

  pyautogui.moveTo(barX, barY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(1)