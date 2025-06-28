import time
import datetime
import random
import pyautogui


print("Position your mouse on the first position")
time.sleep(3)
oneX, oneY = pyautogui.position()

print("Position your mouse on the second position")
time.sleep(3)
twoX, twoY = pyautogui.position()


print("First position: ", oneX, oneY)
print("Second position: ", twoX, twoY)

print("Difference in X: ", twoX - oneX)
print("Difference in Y: ", twoY - oneY)