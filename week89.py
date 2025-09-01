# todo : 같은 화면을 여러 레이아웃으로 배치해보기.
# todo : 3x3 빙고게임 만들어보기. 함수만들고 온클릭하면 O->X  X->O

import tkinter as tk

# 루트창 생성
root = tk.Tk()
root.title("난 고3이다")  # 루트타이틀 지정
root.geometry("300x300")

buttons = []

for row in range(3):
    for column in range(3):

        button = tk.Button(root, text="O", font=(
            "Arial", 20), height=6, width=15, fg="blue", bg="white")

        button.grid(row=row, column=column, sticky="nsew")

        buttons.append(button)
        

for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# 3x3
# O X O
# X O O
# X X X


# 이벤트 루프 실행
root.mainloop()

# ================
# Tip.

# 정의로 이동하기!
#  => ctrl + 클릭


# ================
# 에러 모음

# AttributeError: module 'tkinter' has no attribute 'text'. Did you mean: 'Text'?
# TclError: bad side "bottom,": must be top, bottom, left, or right
# TclError: cannot use geometry manager grid inside . which already has slaves managed by pack
# ================