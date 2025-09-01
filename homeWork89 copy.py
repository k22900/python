
import tkinter as tk
from tkinter import messagebox


# def isDiagonal(status, buttons):
#     for i in range(len(status)):
#         if status[i][i] == 0:
#             return False
#     # 빙고 시, 해당 대각선 버튼 배경 변경
#     print("대각선 1번 빙고")
#     for i in range(len(status)):
#         buttons[i][i].config(bg="green")
#     return True

# def isReverseDiagonal(status, buttons):
#     l = len(status)
#     for i in range(l):
#         if status[l-1-i][i] == 0:
#             return False
#     print("대각선 2번 빙고")
#     for i in range(l):
#         buttons[l-1-i][i].config(bg="green")
#     return True


def isDiagonal(status):
    # 빙고 판단: 오른쪽 아래 방향 대각선 검사
    size = len(status)
    if all(status[i][i]for i in range(size)):
        return [(i, i)for i in range(size)]
    return []


def isReverseDiagonal(status):
    # 빙고 판단: 오른쪽 위 방향 대각선 검사
    size = len(status)
    if all(status[size-1-i][i]for i in range(size)):
        return [(size-1-i, i)for i in range(size)]
    return []


def isRow(status):
    # 행 단위로 검사
    resultPositions = []
    for r, row in enumerate(status):
        if all(value == 1 for value in row):
            # r 번째 행 이 빙고
            resultPositions.extend([(r, c) for c in range(len(row))])
    return resultPositions


def isColumn(status):
    size = len(status)
    resultPositions = []
    for col in range(size):
        if all(status[row][col] == 1 for row in range(size)):
            # col번째 열 전체가 빙고
            resultPositions.extend([(row, col) for row in range(size)])
    return resultPositions


# 빙고 검사 통합 함수

def resetBackground(status):
    size = len(status)
    for r in range(size):
        for c in range(size):
            buttons[r][c].config(bg="white")


def checkBingo(status, buttons):
    # 1) 모든 버튼의 배경을 일단 흰색으로 초기화
    # 2) 빙고 인  녀석(행, 열, 대각선) 초록색으로 .

    # 1) 모든 버튼의 배경을 일단 흰색으로 초기화
    resetBackground(status)

    rowPositions = isRow(status)
    
    columnPositions = isColumn(status)
    
    diagonalPositions = isDiagonal(status)
    
    reverseDiagonalPositions = isReverseDiagonal(status)


    all_positions = rowPositions + columnPositions + \
        diagonalPositions + reverseDiagonalPositions

    # 2) 빙고 인  녀석(행, 열, 대각선) 초록색으로 .
    for (r, c) in all_positions:
        buttons[r][c].config(bg="green")


root = tk.Tk()
root.title("3x3 빙고게임")
root.geometry("600x600")

# 빙고 상태를 저장하는 2차원 리스트
bingoStatus = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def onClick(buttonState, x, y):

    # 버튼 클릭시 0->1, 1->0 으로 전환
    # X -> O

    if buttonState["text"] == "X":
        buttonState.config(text="O", fg="blue")
        bingoStatus[y][x] = 1
    elif buttonState["text"] == "O":
        buttonState.config(text="X", fg="red")
        bingoStatus[y][x] = 0

    # 빙고 검사
    checkBingo(bingoStatus, buttons)


buttons = []
for row in range(3):
    col_arr = []
    for col in range(3):
        btn = tk.Button(root,
                        text="X",
                        font=("Arial", 60),
                        height=3,
                        width=6,
                        fg="red", bg="white",
                        command=lambda r=row, c=col: onClick(buttons[r][c], c, r))
        btn.grid(row=row, column=col, sticky="nsew")
        col_arr.append(btn)
    buttons.append(col_arr)

# 행과 열 균등 분배
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()



# button1=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button1 or a))
# button2=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button2 or a))
# button3=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button3 or a))
# button4=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button4 or a))
# button5=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button5 or a))
# button6=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button6 or a))
# button7=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button7 or a))
# button8=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button8 or a))
# button9=tk.Button(root,text=" ",font=("Arial", 60),height=6,width=15,fg="blue",bg="white",command=lambda a=None: onClick(button9 or a))


# button1.grid(row=0, column=0, sticky="nsew")
# button2.grid(row=0, column=1, sticky="nsew")
# button3.grid(row=0, column=2, sticky="nsew")
# button4.grid(row=1, column=0, sticky="nsew")
# button5.grid(row=1, column=1, sticky="nsew")
# button6.grid(row=1, column=2, sticky="nsew")
# button7.grid(row=2, column=0, sticky="nsew")
# button8.grid(row=2, column=1, sticky="nsew")
# button9.grid(row=2, column=2, sticky="nsew")


