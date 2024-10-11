# 약수에서 자기자신을 제외한수의합이 본인인경우
def PerfactNum(targetNum):
    nums=[]
    for i in range(1,targetNum):
        if targetNum%i==0:
            print(i)
            nums.append(i)
    if sum(nums)==n:
        print(nums)
        print(len(nums))
        return True
        
    else:
        print(nums)
        print(len(nums))
        return False


n=int(input())

if PerfactNum(n):
    print(f"{n}은 완전수이다.")
else:
    print(f"{n}은 완전수가 아니다.")
