import time
import datetime
import random
import pyautogui

#Get the item spots
karamjaGloves = pyautogui.locateCenterOnScreen('fishing/karamjaGloves.png', grayscale=True, confidence=0.8)
homeTab = pyautogui.locateCenterOnScreen('fishing/homeTab.png', grayscale=True, confidence=0.8)

# print("Place your cursor over the Karamja gloves.")
# time.sleep(3)
# karamjaX, karamjaY = pyautogui.position()

# print("Place your cursor over the home teleport")
# time.sleep(3)
# homeX, homeY = pyautogui.position()

print("Starting now!")

loops = 100

for x in range(loops):
  fishingSpot = pyautogui.locateCenterOnScreen('fishing/fishingSpot.png', grayscale=True, confidence=0.9)
  time.sleep(0.5)
  
  pyautogui.click((fishingSpot[0] + random.random()) / 2, (fishingSpot[1] + random.random()) / 2)
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(90)

  pyautogui.click((karamjaGloves[0] + random.random()) / 2, (karamjaGloves[1] + random.random()) / 2)
  time.sleep(6)

  bankChest = pyautogui.locateCenterOnScreen('fishing/bankChest.png', grayscale=True, confidence=0.5)
  time.sleep(0.5)

  pyautogui.click((bankChest[0] + random.random()) / 2, (bankChest[1] + random.random()) / 2)
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(3)

  deposit = pyautogui.locateCenterOnScreen('fishing/depositButton.png', grayscale=True, confidence=0.9)
  time.sleep(0.5)

  pyautogui.click((deposit[0] + random.random()) / 2, (deposit[1] + random.random()) / 2)
  time.sleep(1.5)

  pyautogui.press("esc")
  time.sleep(1)
  
  pyautogui.click((homeTab[0] + random.random()) / 2, (homeTab[1] + random.random()) / 2)
  time.sleep(5)

  fairyRing = pyautogui.locateCenterOnScreen('fishing/fairyRing.png', grayscale=True, confidence=0.5)
  time.sleep(0.5)

  pyautogui.click((fairyRing[0] + random.random()) / 2, (fairyRing[1] + random.random()) / 2)
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(7)