import time
import random
import pyautogui

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Make sure to position your mouse on the tree you want to cut!")
time.sleep(3)
print("Starting in:")
for x in range(3, 0, -1):
    print(str(x) + "...")
    time.sleep(1)
print("Starting now!")

# This will be the position that continually clicks to cut wood
clickX, clickY = pyautogui.position()

for x in range(125):
  print('Running loop #' + str(x + 1))
  for y in range(10):
    pyautogui.moveTo(clickX + (random.random() * 10), clickY + (random.random() * 10))
    time.sleep(random.random() + 0.25)
    pyautogui.click()
    time.sleep((random.random() * 3) + 10)


  logs = list(pyautogui.locateAllOnScreen('woodcutting/blisterwoodlog2.png', grayscale=True))
  for z in range(len(logs)):
      oreX, oreY = pyautogui.center(logs[z])
      pyautogui.keyDown('shift')
      pyautogui.click((oreX + random.random()) / 2, (oreY + random.random()) / 2)
      time.sleep(0.5)
      pyautogui.keyUp('shift')
  time.sleep(0.1)

