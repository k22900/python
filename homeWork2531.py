# 조건1:벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹어야 한다
# 조건2:쿠폰에 적힌 초밥이 현재 벨트 위 없다 = 요리사가 새로 만들은 뒤 손님 제공
# sushiNum=초밥접시수
# sushis=초밥가지수
# sushiPlate=연속으로 먹어야하는 접시수
# coupon=쿠폰번호
# cnt=쿠폰번호에 해당하는 초밥의 중복개수


sushiNum,sushis,sushiPlate,coupon=map(int,input().split())
cnt=0
beltSushi=[]
for _ in range(sushiNum):
    res=int(input())
    if res==coupon:
        cnt+=1
    beltSushi.append(res)

if cnt==1:
    sum=sushiPlate+1
    print(sum)    
elif cnt>1:
    print(sushiPlate)

