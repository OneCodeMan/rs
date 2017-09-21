import pyautogui
import time
from random import randint

RUNNING = True
mouse_pos = (1363, 375)
law_rune_count = 180
spell_count = 0

print("spell count start: " + str(spell_count))
while spell_count < law_rune_count:
    pyautogui.moveTo(x=mouse_pos[0], y=mouse_pos[1])
    pyautogui.click()
    time.sleep(randint(2, 4))
    spell_count += 1
    print(spell_count)

print("spell count end: " + str(spell_count))
