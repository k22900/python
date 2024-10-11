# n//2마리를 데려갈수있고 최대한 많은 종류를 데려가려할때의 종류의 수는?
nums=list(map(int,input().split()))
answer = min(len(set(nums)),len(nums)//2) 
print(answer)