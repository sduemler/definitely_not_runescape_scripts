import time
import random
import pyautogui

barDict = {
  1: "Steel",
  2: "Mithril",
  3: "Adamant",
  4: "Rune"
}

furnaceDict = {
  1: "5",
  2: "7",
  3: "8",
  4: "9"
}

print("Choices:")
for x in barDict.keys():
  print(str(x) + " = " + barDict[x])

barType = input("Which bar type do you want to smith? ")
print("Will be smithing " + barDict[int(barType)] + ".")

print("Start with your character in front of the edgeville furnace.")
time.sleep(1)

print("Getting the position of your coal bag")
time.sleep(3)
coalBagX, coalBagY = pyautogui.position()

print("Place your cursor over the bank booth")
time.sleep(10)
bankX, bankY = pyautogui.position()

print("Now when standing in front of the bank, hover your mouse on the stand.")
time.sleep(3)
bankNearX, bankNearY = pyautogui.position()

print("Place your cursor over the ore you want to smith with the coal one space to the right.")
time.sleep(5)
oreX, oreY = pyautogui.position()
coalX = oreX + 40
coalY = oreY

print("Now for the deposit button")
time.sleep(3)
depositX, depositY = pyautogui.position()

print("Place your cursor over the furnace")
time.sleep(3)
furnaceX, furnaceY = pyautogui.position()

print("Starting now!")

loops = 200

for x in range(loops):
  pyautogui.moveTo(furnaceX, furnaceY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to furnace
  time.sleep(6)

  pyautogui.press(furnaceDict[int(barType)])

  # Smelting
  time.sleep(24)

  pyautogui.moveTo(bankX, bankY)
  time.sleep(0.1)
  pyautogui.click()

  # Running to bank
  time.sleep(6)

  pyautogui.moveTo(depositX, depositY)
  time.sleep(0.5)
  pyautogui.click()

  pyautogui.moveTo(oreX, oreY)
  time.sleep(0.1)
  pyautogui.click()

  time.sleep(1)
  pyautogui.press("esc")

  for y in range(3):
    pyautogui.moveTo(bankNearX, bankNearY)
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.moveTo(coalX, coalY)
    time.sleep(0.1)
    pyautogui.click()

    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)

    pyautogui.moveTo(coalBagX, coalBagY)
    time.sleep(0.1)
    pyautogui.click()
  