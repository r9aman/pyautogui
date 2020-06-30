import pyautogui

print((pyautogui.locateCenterOnScreen("one.png", grayscale=False)))
print((pyautogui.locateCenterOnScreen("plus.png", grayscale=False)))
print((pyautogui.locateCenterOnScreen("two.png", grayscale=False)))
print((pyautogui.locateCenterOnScreen("equal.png", grayscale=False)))


pyautogui.click((pyautogui.locateCenterOnScreen("one.png", grayscale=False)))
pyautogui.click((pyautogui.locateCenterOnScreen("plus.png", grayscale=False)))
pyautogui.click((pyautogui.locateCenterOnScreen("two.png", grayscale=False)))
pyautogui.click((pyautogui.locateCenterOnScreen("equal.png", grayscale=False)))
#pyautogui.press("equal", grayscale=False)
