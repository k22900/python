# html=문서,정적인것
# js= html 문서에 동적인 역할
# css= html 문서에 스타일 

# protocol=관례
# http = 웹 통신 규격 (req, res)

# requests lib = 파이썬에서 http 요청을 보낼 수 있도록.
# beatifulSoup lib = html 문서 를 파싱하여 특정 데이터를 추출 
# Selenium lib = 웹브라우저를 자동화. 동적으로 로드되는 데이터들 처리 (버튼 클릭, 입력)

# pyAutoGUI

# pip install pyautogui
# ctypes
# import time
# from ctypes import wintypes

# wintypes.ULONG_PTR = wintypes.WPARAM
# hllDll = ctypes.WinDLL ("User32.dll", use_last_error=True)
# VK_HANGUEL = 0x15

import pyautogui as tracking

def korEngSwitch():
    tracking.hotkey('win','space')

def chromeExecution():
    tracking.hotkey('win','s')
    tracking.typewrite(" Chrome",0.1)
    tracking.typewrite(['enter'])

def webAccess():
    tracking.sleep(1)
    tracking.hotkey('win','up')
    tracking.moveTo(264,56,3)
    tracking.click()
    tracking.typewrite("https://www.naver.com",0.01)
    tracking.typewrite(['enter'])

def screenShotHotkey():
    tracking.hotkey('win','shift','s')
    tracking.click()

# while 1:
# tracking.moveTo(0,300,2) # 0,300 로 간다.
# tracking.moveRel(0,300,2) # 현재+0, 현재+300
                # pos = pyautogui.position()
    # print(pos)

# tracking.position
# tracking.moveTo(545,830,3)
# tracking.click()
# tracking.typewrite("cd res")
# tracking.typewrite(['enter'])
# tracking.typewrite("cd ..")
# tracking.typewrite(['enter'])
# tracking.moveTo(363,1056,3)

korEngSwitch()
# tracking.hotkey('win','space')

chromeExecution()
# tracking.hotkey('win','s')
# tracking.typewrite(" Chrome",0.1)
# tracking.typewrite(['enter'])

webAccess()
# tracking.moveTo(264,56)
# tracking.click()
# tracking.typewrite("https://www.naver.com",0.0000001)
# tracking.typewrite(['enter'])

korEngSwitch()
# tracking.hotkey('win','space')

# screenShotHotkey()
# tracking.hotkey('ctrl','N')


