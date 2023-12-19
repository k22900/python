# for i in range(0,10,1):
#     for j in range(0,10,1):
#         if i+j<=9 and i+j>=0:
#             print("*",end=" ")
#     print()
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    for _ in range(i):
        print(end="  ")
    for j in range(5-i):
        print("*",end="")
    print()
for i in range(4):
    for j in range(2+i):
        print("*",end="")
    for _ in range(3-i):
        print(end="  ")
    for j in range(2+i):
        print("*",end="")
    print()        