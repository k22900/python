# 
citations=[3, 0, 6, 1, 5]
citations.sort()
for idx,val in enumerate(citations):
    num=len(citations[idx:])
    if val==num:
        answer=val
        break
print(answer)