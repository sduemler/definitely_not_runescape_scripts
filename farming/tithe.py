import time
import datetime
import random
import pyautogui

start = time.time()

print("Start with your character on the marked tile in front of the LAST plant")

print("Position your mouse on the seeds in your inventory")
time.sleep(2)
seedsX, seedsY = pyautogui.position()

print("Position your mouse on a watering can in your inventory")
time.sleep(2)
canX, canY = pyautogui.position()

print("Position your mouse on the first tile")
time.sleep(3)
returnX, returnY = pyautogui.position()

time.sleep(3)
print("Place your mouse over the position of the water barrel.")
time.sleep(3)
barrelX, barrelY = pyautogui.position()

print("Now run to the left tile of it")
time.sleep(5)

print("Position your mouse of the first marked tile")
time.sleep(3)
restartX, restartY = pyautogui.position()

print("Now run to the first marked tile")
time.sleep(10)

print("Finally, place your mouse of the first tithe patch")
time.sleep(3)
titheX, titheY = pyautogui.position()

tithe2X = titheX - 150
tithe2Y = titheY

tithe3X = tithe2X + 170
tithe3Y = tithe2Y + 90

print("Starting now!")

loops = 65

def firstPatch(onlyWater):
    if not onlyWater:
        # Plant seeds
        pyautogui.moveTo(seedsX + (random.random() * 2), seedsY + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        pyautogui.moveTo(titheX + (random.random() * 2), titheY + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        time.sleep(2)

    # Water
    pyautogui.moveTo(titheX + (random.random() * 2), titheY + (random.random() * 2))
    time.sleep(random.random() + 0.25)
    pyautogui.click()

    time.sleep(2)


def secondPatch(onlyWater):
    if not onlyWater:
        pyautogui.moveTo(seedsX + (random.random() * 2), seedsY + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        pyautogui.moveTo(tithe2X + (random.random() * 2), tithe2Y + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        time.sleep(3)

    else:
        time.sleep(5)
        
    # Water
    pyautogui.moveTo(tithe2X + (random.random() * 2), tithe2Y + (random.random() * 2))
    time.sleep(random.random() + 0.25)
    pyautogui.click()

    time.sleep(2)
   
def thirdPatch(onlyWater):
    if not onlyWater:
        pyautogui.moveTo(seedsX + (random.random() * 2), seedsY + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        pyautogui.moveTo(tithe3X + (random.random() * 2), tithe3Y + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        time.sleep(3)

        # Water
        pyautogui.moveTo(titheX + (random.random() * 2), titheY + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        time.sleep(2)
    else:
        time.sleep(5)
        pyautogui.moveTo(tithe3X + (random.random() * 2), tithe3Y + (random.random() * 2))
        time.sleep(random.random() + 0.25)
        pyautogui.click()

        time.sleep(2)


for x in range(loops):
    for y in range(4):
        onlyWater = True
        if y == 0:
            onlyWater = False
        firstPatch(onlyWater)
        secondPatch(onlyWater)
        thirdPatch(onlyWater)
        secondPatch(onlyWater)
        thirdPatch(onlyWater)
        secondPatch(onlyWater)
        thirdPatch(onlyWater)
        secondPatch(onlyWater)
        if y == 3:
            pyautogui.moveTo(canX + (random.random() * 2), canY + (random.random() * 2))
            time.sleep(random.random() + 0.25)
            pyautogui.click()

            time.sleep(1)

            pyautogui.moveTo(barrelX + (random.random() * 2), barrelY + (random.random() * 2))
            time.sleep(random.random() + 0.25)
            pyautogui.click()
            time.sleep(15)

            pyautogui.moveTo(restartX, restartY)
            time.sleep(1)
            pyautogui.click()
            time.sleep(5)

        else:
            pyautogui.moveTo(returnX, returnY)
            time.sleep(1)
            pyautogui.click()
            time.sleep(10)
    


now = datetime.datetime.now()

print("Logging out at: ", now)