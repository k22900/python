import re
import threading
import pyautogui
from pynput import mouse

isRunning = True

def onRightClick(x,y,button,pressed):
    global isRunning
    if button == mouse.Button.right and pressed:
        if isRunning:
            print("우클릭 감지: 좌클릭 멈춤")
            isRunning = False
        else:
            print("우클릭 감지: 좌클릭 시작")
            isRunning = True

def autoLeftClick():
    global isRunning
    while True:
        while isRunning:    
            print("좌클릭 감지")
            # pyautogui.click(interval=0.3)
            pyautogui.leftClick()



listener = mouse.Listener(on_click=onRightClick)
listener.start()

otherThread = threading.Thread(target=autoLeftClick)
otherThread.start()

