import time, threading, pyautogui, keyboard, os

def recordloc():
    global x, y
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        time.sleep(5)
        x = currentMouseX
        y = currentMouseY
        print('recorded loc')
        print(f"{x}, " + f"{y}")

def goback():
    global x, y
    def gobackplz():
        pyautogui.moveTo(x,y)
        print('it tried it')
    keyboard.add_hotkey('ctrl+shift+a', lambda: gobackplz())
    keyboard.wait()

def iwnagonow():
    keyboard.add_hotkey('esc', lambda: os._exit(0))

threads = [threading.Thread(target=recordloc),threading.Thread(target=goback),threading.Thread(target=iwnagonow)]

for thread in threads:
    thread.start()
