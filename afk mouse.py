import pyautogui as pag
import random, time  # noqa: E401


pag.FAILSAFE = False
while True:
    
    x = random.randint(0, 6000)
    y = random.randint(0, 1000)
    pag.moveTo(x, y, 0.5)
    time.sleep(0.5)
    pag.click()
