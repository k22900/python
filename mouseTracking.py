import pyautogui
import tkinter as tk
# from tkinter import messagebox
while 1:
    # root=tk.Tk()

    # root.title("마우스 위치좌표확인인")
    # root.geometry("150x150")

    pos=pyautogui.position()
    # label1=tk.Label(root,text=str(pos),fg="black",bg="red")
    # label1.pack()
    print(pos)
    # root.mainloop()