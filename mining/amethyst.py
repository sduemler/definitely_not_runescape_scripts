import time
import datetime
import random
import pyautogui

start = time.time()

#Locate knife in the inventory, fails if it can't find it
chiselX, chiselY = pyautogui.locateCenterOnScreen('mining/chisel.png', grayscale=True, confidence=0.9)

# #Get the logout X
# print("Place your cursor over the logout X.")
# time.sleep(3)
# xX, yX = pyautogui.position()

# print("Place your cursor over the logout button.")
# time.sleep(3)
# logoutX, logoutY = pyautogui.position()

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Start with your character in the middle of 3 amethyst rocks.")
print("Position your mouse the amethyst in front of you")
time.sleep(3)
position1X, position1Y = pyautogui.position()
print("Click on the amethyst next to you.")
time.sleep(3)
position2X, position2Y = pyautogui.position()
time.sleep(1)
print("Place your mouse over the position of the other amethyst rock.")
time.sleep(3)
resetX, resetY = pyautogui.position()
time.sleep(1)

print("Walk back to your starting position")
time.sleep(3)

print("Starting now!")

waitTime = 50
loops = 80
chisel = 0

pyautogui.moveTo(position1X + (random.random() * 2), position1Y + (random.random() * 2))
time.sleep(random.random() + 0.25)
pyautogui.click()

time.sleep(waitTime)

for x in range(loops):
  pyautogui.moveTo(position2X + (random.random() * 2), position2Y + (random.random() * 2))

  time.sleep(random.random() + 0.25)
  pyautogui.click()

  time.sleep(waitTime + random.random() * 10)

  pyautogui.moveTo(resetX + (random.random() * 2), resetY + (random.random() * 2))

  time.sleep(random.random() + 0.25)
  pyautogui.click()

  time.sleep(waitTime + random.random() * 10)

  pyautogui.moveTo(position2X + (random.random() * 2), position2Y + (random.random() * 2))

  time.sleep(random.random() + 0.25)
  pyautogui.click()

  time.sleep(waitTime + random.random() * 10)

  chisel = chisel + 1

  if chisel % 5 == 0:
    amethystX, amethystY = pyautogui.locateCenterOnScreen('mining/amethyst.png', grayscale=True, confidence=0.9)
    
    pyautogui.click(chiselX / 2, chiselY / 2)
    time.sleep(random.random() + 1)
    pyautogui.click(amethystX / 2, amethystY / 2)
    time.sleep(random.random() + 2)
    pyautogui.press('space')

    time.sleep(30)

  


#Logging out
pyautogui.moveTo(xX, yX)
time.sleep(0.3)
pyautogui.click()

pyautogui.moveTo(logoutX, logoutY)
time.sleep(0.3)
pyautogui.click()


now = datetime.datetime.now()

print("Logging out at: ", now)