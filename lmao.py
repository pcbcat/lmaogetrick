import pyautogui
import time
pyautogui.hotkey("win")
pyautogui.typewrite("run", interval=0.04)
pyautogui.press("enter", interval=0.04)
pyautogui.typewrite("https://www.youtube.com/watch?v=dQw4w9WgXcQ", interval=0.04)
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.alert(text='lmao get rick', title='lmao', button='OK')