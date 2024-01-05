import time
import random
import pyautogui

start = time.time()

#Locate knife in the inventory, fails if it can't find it
knifeX, knifeY = pyautogui.locateCenterOnScreen('fletching/runescape_knife.png', grayscale=True)

#Get the logout X
print("Place your cursor over the logout X.")
time.sleep(3)
xX, yX = pyautogui.position()

print("Place your cursor over the logout button.")
time.sleep(3)
logoutX, logoutY = pyautogui.position()

# Gives the user time to place the cursor where they want to continually click for woodcutting
print("Position your mouse over the first set of redwood.")
time.sleep(3)
position1X, position1Y = pyautogui.position()
print("Position your mouse over the second set of redwood.")
time.sleep(3)
position2X, position2Y = pyautogui.position()
time.sleep(1)
pyautogui.press('f4')
print("Place your mouse over the position of the high alchemy spell.")
time.sleep(3)
alchX, alchY = pyautogui.position()
time.sleep(1)
pyautogui.press('f3')

print("Starting now!")

#28 loops gets you to about 5 hours 45 minutes of play
loops = 28

for x in range(loops):
  print('Running loop #' + str(x + 1) + ' out of ' + str(loops))

  if x == 0:
    pyautogui.moveTo(position1X + (random.random() * 3), position1Y + (random.random() * 3))
  else:
    pyautogui.moveTo(position1X + (position1X - position2X), position1Y  + (random.random() * 3))
  time.sleep(random.random() + 0.25)
  pyautogui.click()

  #Sleep for 5 minutes while chopping, on average how long one spot lasts
  time.sleep(300)

  pyautogui.moveTo(position2X + (random.random() * 3), position2Y + (random.random() * 3))
  time.sleep(random.random() + 0.25)
  pyautogui.click()

  time.sleep(300)

  #Fletching into redwood shields
  logs = list(pyautogui.locateAllOnScreen('woodcutting/redwoodlog.png', grayscale=True))
  logX, logY = pyautogui.center(logs[len(logs) - 1])

  pyautogui.click(knifeX / 2, knifeY / 2)
  time.sleep(random.random() + 1)
  pyautogui.click(logX / 2, logY / 2)
  time.sleep(random.random() + 2)
  pyautogui.press('space')

  time.sleep(60)

  #Alching the shields
  #Locate the shields
  shields = list(pyautogui.locateAllOnScreen('woodcutting/redwoodshield.png', grayscale=True, confidence=0.9))

  pyautogui.press('f4')
  time.sleep(0.5)

  for y in range(len(shields)):
    pyautogui.click(alchX, alchY)
    time.sleep(1.5)
    shieldX, shieldY = pyautogui.center(shields[y])
    pyautogui.click(shieldX / 2, shieldY / 2)
    time.sleep(1.5)
  
  pyautogui.press('f3')
  
#Logging out
print("Logging out now.")
pyautogui.moveTo(xX, yX)
time.sleep(0.3)
pyautogui.click()

pyautogui.moveTo(logoutX, logoutY)
time.sleep(0.3)
pyautogui.click()

end = time.time()
elapsed = ((end - start) / 60) / 60

print("You were woodcutting for " + str(elapsed) + " hours.")
