import time
import random
import pyautogui


print("Now starting recording of agility lap.")
print("Start at the end of the last zipline.")
time.sleep(10)
firstX, firstY = pyautogui.position()

print("Second Obstacle")
time.sleep(25)
secondX, secondY = pyautogui.position()

print("Third Obstacle")
time.sleep(5)
thirdX, thirdY = pyautogui.position()

print("Fourth Obstacle")
time.sleep(10)
fourthX, fourthY = pyautogui.position()

print("Fifth Obstacle")
time.sleep(25)
fifthX, fifthY = pyautogui.position()

print("Sixth Obstacle")
time.sleep(10)
sixthX, sixthY = pyautogui.position()


print("Starting now!")
time.sleep(3)


#Running loop
for x in range(300):
  pyautogui.moveTo(firstX + random.random(), firstY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(5.5)

  pyautogui.moveTo(secondX + random.random(), secondY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(21)

  pyautogui.moveTo(thirdX + random.random(), thirdY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(4)

  pyautogui.moveTo(fourthX + random.random(), fourthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(6.5)

  pyautogui.moveTo(fifthX + random.random(), fifthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(21)

  pyautogui.moveTo(sixthX + random.random(), sixthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(11)