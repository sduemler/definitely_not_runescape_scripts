import time
import random
import pyautogui


#Get the logout X
print("Place your cursor over the logout X.")
time.sleep(3)
xX, yX = pyautogui.position()

print("Place your cursor over the logout button.")
time.sleep(3)
logoutX, logoutY = pyautogui.position()

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


#140 runs is usually just under 6 hours to prevent auto logging
for x in range(140):
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

#Logging out
print("Logging out now.")
pyautogui.moveTo(xX, yX)
time.sleep(0.3)
pyautogui.click()

pyautogui.moveTo(logoutX, logoutY)
time.sleep(0.3)
pyautogui.click()

print("Logged out.")

