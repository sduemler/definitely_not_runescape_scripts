import time
import datetime
import random
import pyautogui

#Get the logout X
print("Place your cursor over the fishing spot.")
time.sleep(3)
fishingX, fishingY = pyautogui.position()

print("Starting now!")

loops = 100

for x in range(loops):
  pyautogui.moveTo(fishingX, fishingY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(90)

  fish = list(pyautogui.locateAllOnScreen('fishing/karambwan.png', grayscale=True, confidence=0.9))

  time.sleep(0.5)

  for y in range(len(fish)):
    fishX, fishY = pyautogui.center(fish[y])
    pyautogui.keyDown('shift')
    pyautogui.click((fishX + random.random()) / 2, (fishY + random.random()) / 2)
    time.sleep(0.5)
    pyautogui.keyUp('shift')