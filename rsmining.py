# control + c to stop running
import pyautogui
import time

# has limitations
def clear_inventory(inventory_icon, first_ore):
  pyautogui.click(x=inventory_icon[0], y=inventory_icon[1])
  ore_dx = 42 # change in x in inventory
  ore_dy = 34 # change in y in inventory
  drop_factor = 36
  x_pos_inv = first_ore[0]
  for j in range(4):
    y_pos_inv = first_ore[1]
    for k in range(6):
	  # right click
      pyautogui.rightClick(x=x_pos_inv, y=y_pos_inv)
	  # move mouse to drop option
      pyautogui.moveTo(x=x_pos_inv, y=y_pos_inv+drop_factor)
	  # left click to drop
      pyautogui.click()
	  # move mouse back up
      pyautogui.moveTo(x=x_pos_inv, y=y_pos_inv)
	  # move to the bottom
      y_pos_inv += ore_dy
    x_pos_inv += ore_dx

def one_ore(time_limit, ore_location):
  while time.time() < time_limit:
    pyautogui.click(x=ore_location[0], y=ore_location[1], clicks=1, interval=15, button='left')

def three_ores(time_limit, ores):
  while time.time() < time_limit:
    pyautogui.click(x=ores[0][0], y=ores[0][1], clicks=1, interval=3, button='left')
    time.sleep(3)
    pyautogui.click(x=ores[1][0], y=ores[1][1], clicks=1, interval=7, button='left')
    pyautogui.click(x=ores[2][0], y=ores[2][1], clicks=1, interval=11, button='left')

def two_ores(time_limit, ore1, ore2):
    while time.time() < time_limit:
        pyautogui.click(x=ore1[0], y=ore1[1], clicks=1, interval=3, button='left')
        time.sleep(2)
        pyautogui.click(x=ore2[0], y=ore2[1], clicks=1, interval=7, button='left')

def last_two(pos):
    ore_dx = 42
    ore_dy = 34

    pyautogui.rightClick(pos[0], pos[1])

    pyautogui.moveTo(x=pos[0], y=pos[1]+20)

    pyautogui.click()

    pyautogui.moveTo(x=pos[0], y=pos[1])

    pyautogui.rightClick(pos[0] + 42, y=pos[1])

    pyautogui.moveTo(x=pos[0] + 42, y=pos[1] + 20)

    pyautogui.click()

    pyautogui.rightClick(pos[0] + 84, y=pos[1])

    pyautogui.moveTo(x=pos[0] + 84, y=pos[1] + 20)

    pyautogui.click()

# VARIABLES THAT CHANGE
ore_location = (829, 196) # this is the coordinate of the ore i'm clicking on
ores = ((871, 183), (990, 223))
first_ore_in_inv = (1254, 303) # this is the coordinate of first ore in inventory
inventory_icon = (1318, 259)
minutes_mining = 4 # this might change often
last_two_pos = (1295, 520)

# CONSTANTS
RUNNING = True
DURATION_MINING = time.time() + 60 * minutes_mining # just more readable


while RUNNING:

  two_ores(DURATION_MINING, ores[0], ores[1])

  clear_inventory(inventory_icon, first_ore_in_inv)
  last_two(last_two_pos)
  DURATION_MINING = time.time() + 60 * minutes_mining # just more readable
  time.sleep(2)



clear_inventory(inventory_icon, first_ore_in_inv)
last_two(last_two_pos)
