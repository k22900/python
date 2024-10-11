# 전화번호부 안에 번호들중 어떤번호가 다른번호에 접두어로 있는지 찾는다 
phone_book=["119", "97674223", "1195524421"]
from collections import defaultdict
phone_book_dict=defaultdict(int)
for val in phone_book:
    phone_book_dict[val]+=1
print(phone_book_dict)
# if phone_book[0] in phone_book_dict:
#     answer=False
# else:
#     answer=True
# print(answer)