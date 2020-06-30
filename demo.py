import pyautogui
import time

pyautogui.FAILSAFE = True

# print(pyautogui.size())


pyautogui.hotkey('win')
pyautogui.press('enter')
pyautogui.write("chrome")
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
pyautogui.write("www.youtube.com")
pyautogui.press('enter')
