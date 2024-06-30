import time
import random
import pyautogui

timings = [7, 10, 5, 6.2, 4, 17]
obstacles = []

def moveToObstacle(timing, point):
  pyautogui.moveTo(point[0] + random.random(), point[1] + random.random())
  time.sleep(0.1)
  pyautogui.click()
  time.sleep(timing)

print("Now starting recording of agility lap.")
print("After climbing onto the rooftop, place your cursor over the first obstacle.")
time.sleep(15)
x1, y1 = pyautogui.position()
obstacles.append((x1, y1))

print("Second Obstacle")
time.sleep(15)
x2, y2 = pyautogui.position()
obstacles.append((x2, y2))

print("Third Obstacle")
time.sleep(10)
x3, y3 = pyautogui.position()
obstacles.append((x3, y3))

print("Fourth Obstacle")
time.sleep(10)
x4, y4 = pyautogui.position()
obstacles.append((x4, y4))

print("Fifth Obstacle")
time.sleep(10)
x5, y5 = pyautogui.position()
obstacles.append((x5, y5))

print("Click on beginning climb")
time.sleep(20)
x6, y6 = pyautogui.position()
obstacles.append((x6, y6))

print("Starting now!")
time.sleep(3)

#Running loop
for x in range(350):
  for z in range(len(obstacles)):
    moveToObstacle(timings[z], obstacles[z])
  