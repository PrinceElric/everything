import pyautogui, time, sys  # noqa: E401  # noqa: E401 
sys.path.append(r"C:\Users\elric\Desktop\vs code\all that")
from tools import *  # noqa: F403
def normal(tps=315):
    while True:
        time.sleep(tps)
        # pyautogui.press('space')  #chrome anime
        time.sleep(0.6)
        pyautogui.hotkey('win', 'm')
        time.sleep(0.6)
        pyautogui.hotkey('win', 'tab')
        time.sleep(0.6)
        pyautogui.moveTo(800, 300)
        pyautogui.click()
        # time.sleep(0.6)
        # # pyautogui.moveTo(650, 1000)
        # # pyautogui.click()
        time.sleep(1.2)
        pyautogui.moveTo(1000, 670)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.moveTo(1000, 970)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.hotkey('win', 'm')
        time.sleep(1)
        pyautogui.moveTo(1230, 1250)
        time.sleep(0.6)
        pyautogui.moveTo(1250, 1170) #vscode
        pyautogui.click() #vscode
        # pyautogui.moveTo(1170, 1170) #chrome
        # pyautogui.click() #chrome
        # time.sleep(0.6) #chrome
        # pyautogui.moveTo(1800, 1000) #chrome
        # pyautogui.click() #chrome
        # time.sleep(0.6) #chrome
        # pyautogui.press('space') #chrome


def full():
    while True:
        pyautogui.moveTo(1000, 670)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.moveTo(1000, 970)
        pyautogui.click()
        time.sleep(0.6)
        time.sleep(10)

def onglet(tps=315):
    while True:
        time.sleep(tps)
        pyautogui.press('space')
        time.sleep(0.6)
        pyautogui.press('esc')
        time.sleep(0.6)
        pyautogui.moveTo(200, 20)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(1000, 670)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.moveTo(1000, 970)
        pyautogui.click()
        time.sleep(0.8)
        pyautogui.moveTo(500, 20)
        pyautogui.click()
        # time.sleep(0.6)
        # pyautogui.moveTo(1850, 1130)
        # pyautogui.click()
        # time.sleep(0.6)
        pyautogui.moveTo(1000, 800)
        # pyautogui.click()
    
def coffre(n):
    time.sleep(7)
    for _ in range(n):
        pyautogui.moveTo(1150, 1000)
        pyautogui.click()
        time.sleep(3.5)

onglet()
