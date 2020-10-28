import pyautogui

x, y = pyautogui.position()
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr)
# print('\b' * len(positionStr), end='', flush=True)
