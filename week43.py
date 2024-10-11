# import cowsay

# cowsay.char



global num 
num = 5

def g():
    print(num, end=" ")#9

def f():
    global num
    num = 9
    while num < 8:
        num += 1
    print(num, end=" ")#9
    g()

f()

print(num, end=" ")#9
