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

# VARIABLES THAT CHANGE
ore_location = (918, 366) # this is the coordinate of the ore i'm clicking on
ores = ((899, 222), (898, 331), (1064, 346))
first_ore_in_inv = (1254, 301) # this is the coordinate of first ore in inventory
inventory_icon = (1318, 259)
minutes_mining = 8 # this might change often

# CONSTANTS
RUNNING = True
DURATION_MINING = time.time() + 60 * minutes_mining # just more readable

#while RUNNING:

  #one_ore(DURATION_MINING, ore_location)
  
  #clear_inventory(inventory_icon, first_ore_in_inv)
  #DURATION_MINING = time.time() + 60 * minutes_mining # just more readable
  #time.sleep(3)

clear_inventory(inventory_icon, first_ore_in_inv)