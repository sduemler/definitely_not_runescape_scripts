import time
import random
import pyautogui

sharks = list(pyautogui.locateAllOnScreen('thieving/shark.png', grayscale=True))
print(str(len(sharks)) + " sharks found")

print("Place your cursor one tile to your right.")
time.sleep(3)
returnX, returnY = pyautogui.position()

#Get the knight location
print("Place your cursor over the splashed knight.")
time.sleep(3)
knightX, knightY = pyautogui.position()

print("Place your cursor over the coin pouch location")
time.sleep(3)
coinX, coinY = pyautogui.position()

eat = False;

#140 runs is usually just under 6 hours to prevent auto logging
while(len(sharks) > 1):
  pyautogui.moveTo(knightX, knightY)
  for x in range(100):
    time.sleep((random.random() / 10) + 1)
    pyautogui.click()
    if (x % 20 == 0):
        pyautogui.moveTo(returnX, returnY)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(knightX, knightY)
  time.sleep(1)
  pyautogui.click()
  time.sleep(1)
  
  # Open coin pouches
  sharks = list(pyautogui.locateAllOnScreen('thieving/shark.png', grayscale=True))
  sharkX, sharkY = pyautogui.center(sharks[0])

  pyautogui.moveTo(coinX, coinY)
  time.sleep(1)
  pyautogui.click()
  time.sleep(1)

  #Eat
  if (eat):
    pyautogui.click((sharkX / 2), (sharkY / 2))
  eat = not eat