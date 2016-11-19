# control + c to stop running
import pyautogui
import time

# has limitations
def clear_inventory(first_ore):
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

# VARIABLES THAT CHANGE
ore_location = (824, 248) # this is the coordinate of the ore i'm clicking on
first_ore = (1216, 303) # this is the coordinate of first ore in inventory
minutes_mining = 3 # this might change often

# CONSTANTS
RUNNING = True
DURATION_MINING = time.time() + 60 * minutes_mining # just more readable

# would use while RUNNING but it's weird


while RUNNING:

  while time.time() < DURATION_MINING:
    pyautogui.click(x=ore_location[0], y=ore_location[1], clicks=1, interval=4, button='left')
  
  clear_inventory(first_ore)
  DURATION_MINING = time.time() + 60 * minutes_mining # just more readable
  time.sleep(3)

