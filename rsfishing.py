# control + c to stop running
import pyautogui
import time

# has limitations
def clear_inventory(inventory_icon, first_ore, cooked):
  pyautogui.click(x=inventory_icon[0], y=inventory_icon[1])
  ore_dx = 42 # change in x in inventory
  ore_dy = 34 # change in y in inventory
  drop_factor = 53 if cooked else 36
  x_pos_inv = first_ore[0]
  i = 0
  the_range = 6
  for j in range(4):
    y_pos_inv = first_ore[1]
    if i == 2:
        the_range = 8
    i += 1
    for k in range(the_range):

      if the_range > 5:
        drop_factor = 30

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


first_fish_in_inv = (1249, 301) # this is the coordinate of first fish in inventory
inventory_icon = (1318, 259)

clear_inventory(inventory_icon, first_fish_in_inv, False)
