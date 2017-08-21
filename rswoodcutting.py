import pyautogui

tree_location = (993, 247)
tree_x, tree_y = tree_location
click_interval = 30

while True:
	pyautogui.click(x=tree_x, y=tree_y, clicks=1, interval=30, button='left')