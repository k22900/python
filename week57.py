_list=[1,8,9,10,10,2,6]
result=_list[0]

for i in _list:
    if i > result:
        result=i

print(result)
list.sort()       