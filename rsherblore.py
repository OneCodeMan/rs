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
  for j in range(4):
    y_pos_inv = first_ore[1]
    for k in range(7):

	  # right click
      pyautogui.moveTo(x=x_pos_inv, y=y_pos_inv)

	  # left click to drop
      pyautogui.click()

	  # move to the bottom
      y_pos_inv += ore_dy
    x_pos_inv += ore_dx

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

first_fish_in_inv = (1249, 301) # this is the coordinate of first fish in inventory
last_two_pos = (1334, 518)
inventory_icon = (1318, 259)

clear_inventory(inventory_icon, first_fish_in_inv, False)
