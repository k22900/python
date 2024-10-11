from collections import Counter
# 한명빼고 다 완주했을때 완주못한선수의 이름을구하자

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

# print(participant,completion,sep="\n")

completCnt=Counter(completion)
partCnt=Counter(participant)
# print(partCnt,completCnt)
answer= partCnt - completCnt

print(answer)
# ____________________________________
# for partIdx,v in enumerate(participant):
#     cnt=0
#     for idx,targetValue in enumerate(completion):
#         if v==targetValue:
#             completion[idx]="/"
#             cnt+=1
#             break
#     if cnt==0:
#         print(str(participant[partIdx]))
#         # answer = 
#         break
# _______________________________________________________________________________