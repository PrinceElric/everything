import pyautogui, time, subprocess, sys  # noqa: E401  # noqa: E401 
from datetime import datetime  # noqa: F401


def copier_txt(texte):
    """copie texte dans presse-papier, need subprocess"""
    subprocess.run(["clip"], input=texte, text=True, check=True)
while True:
    now = datetime.now()
    if now.hour == 23 and now.minute == 59:
        pyautogui.press('space')
        time.sleep(1)
        pyautogui.hotkey("win", "m")
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write("cmd")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(3)
        copier_txt(r'cd "C:\Users\elric\Desktop\vs code\all that\projet_dateAnniv"')
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write("python date.py")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(7)
        pyautogui.write("exit")
        time.sleep(1)
        pyautogui.press("enter")
        sys.exit()
    else:
        time.sleep(0.9)


# x, y = 1745, 666
# pyautogui.moveTo(x, y, 1)
# time.sleep(1)
# pyautogui.click()
