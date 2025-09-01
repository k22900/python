import tkinter as tk

# 루트창 생성
root = tk.Tk()
# # 루트타이틀 지정
# root.title("난 고3이다")
# root.geometry("800x600")

# # tk.Menu()
label1=tk.Label(root,text="난 선생이야",fg="black",bg="red")
# label2=tk.Label(root,text="난 선생이야",fg="black",bg="gray")
# label3=tk.Label(root,text="난 선생이야",fg="black",bg="lightgreen")
# label4=tk.Label(root,text="난 선생이야",fg="black",bg="lightblue")


label1.pack(side="top",padx=100,pady=100)
# # label2.pack(side="bottom",padx=100,pady=100)
# # label3.pack(side="left",padx=100,pady=100)
# # label4.pack(side="right",padx=100,pady=100)


# label1.grid(row=1,column=0,padx="20",pady="20")
# label2.grid(row=1,column=2,padx="20",pady="20")
# label3.grid(row=3,column=0,padx="20",pady="20")
# label4.grid(row=3,column=2,padx="20",pady="20")
 








def onClick():
    button1.config(text="왜 눌러!")

button1=tk.Button(root,text="날 눌러줘",command=onClick)
button1.pack(padx=100,pady=100)

# tk.Text(root,)

# entry1=tk.Entry(root,width=50)
# entry1.pack(padx=100,pady=100)
# label1.grid(row=0,column=0,padx=10,pady=10)
# tk.Checkbutton(root,"-",command="onClick")
# 이벤트 루프 실행
root.mainloop()


