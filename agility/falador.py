import time
import random
import pyautogui


print("Now starting recording of agility lap.")
print("After climbing onto the rooftop, place your cursor over the first obstacle.")
time.sleep(10)
firstX, firstY = pyautogui.position()


print("Second Obstacle")
time.sleep(10)
secondX, secondY = pyautogui.position()

print("Third Obstacle")
time.sleep(10)
thirdX, thirdY = pyautogui.position()

print("Fourth Obstacle")
time.sleep(10)
fourthX, fourthY = pyautogui.position()

print("Fifth Obstacle")
time.sleep(10)
fifthX, fifthY = pyautogui.position()

print("Sixth Obstacle")
time.sleep(10)
sixthX, sixthY = pyautogui.position()

print("Seventh Obstacle")
time.sleep(10)
seventhX, seventhY = pyautogui.position()

print("Eighth Obstacle")
time.sleep(10)
eighthX, eighthY = pyautogui.position()

print("Ninth Obstacle")
time.sleep(10)
ninthX, ninthY = pyautogui.position()

print("Tenth Obstacle")
time.sleep(10)
tenthX, tenthY = pyautogui.position()

print("Eleventh Obstacle")
time.sleep(10)
eleventhX, eleventhY = pyautogui.position()

print("Twelfth Obstacle")
time.sleep(10)
twelfthX, twelfthY = pyautogui.position()

print("Click on beginning climb")
time.sleep(10)
begX, begY = pyautogui.position()

print("Starting now!")
time.sleep(3)


#Running loop
for x in range(300):
  pyautogui.moveTo(firstX + random.random(), firstY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(8.5)

  pyautogui.moveTo(secondX + random.random(), secondY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(10)

  pyautogui.moveTo(thirdX + random.random(), thirdY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(3.5)

  pyautogui.moveTo(fourthX + random.random(), fourthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(3.8)

  pyautogui.moveTo(fifthX + random.random(), fifthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(9.6)

  pyautogui.moveTo(sixthX + random.random(), sixthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(5)

  pyautogui.moveTo(seventhX + random.random(), seventhY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(3)

  pyautogui.moveTo(eighthX + random.random(), eighthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(4)
  
  pyautogui.moveTo(ninthX + random.random(), ninthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(3.3)

  pyautogui.moveTo(tenthX + random.random(), tenthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(4.7)

  pyautogui.moveTo(eleventhX + random.random(), eleventhY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(3.8)

  pyautogui.moveTo(twelfthX + random.random(), twelfthY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(5.9)

  pyautogui.moveTo(begX + random.random(), begY + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(6.2)