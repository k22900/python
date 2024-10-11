
# 입금(돈을 통장에 넣는다)
#   돈의 금액을 입력받는다.
#   액수가 입력 되었으면 통장의 잔고의 그액수를 추가해준다
# 출금(통장에 돈을 현금화 한다)
#   통장의 비밀번호를 확인한다(pass)
#       참이면 원하는 액수를 물어보고 입력받는다
#       액수를 입력 받았으면 권종 선택하게한다
#       선택되었으면 선택한대로 지폐를 반출한다 

#   거짓이면 다시물어본다 
# 예금조회(통장에 돈을 확인한다)
#   통장의 비밀번호를 확인한다(pass)
#       참이면 통장의 잔액을 보연준다
#   거짓이면 다시물어본다
# 송금(다른사람의 통장으로 돈을 보낸다)
#   통장의 비밀번호를 확인한다(pass)
#       참이면 받는 사람의 계좌정보를 입력 받는다
      
# 통장정리(통장에 이용내역을 업데이트한다)
balance=1000

def deposit():
    global balance
    amount=int(input())
    balance+=amount

def withdraw():
    global balance
    value=int(input())
    if balance<value:
        print("잔액이 부족합니다")
    else:
        balance-=value
        print(f"출금후 잔액 |{balance}|원")
def show():
    print(f"현제 잔액은 |{balance}|원입니다")
    print(history)

history=[balance]
while True:
    print("=========곽지민 ATM=========")
    print("입금은 1번 출금은 2번 잔액조회는 3번 업무중단은 4번")
    select=int(input())
    if select==1:
        print(f"입금전 잔액 |{balance}|원")
        deposit()
        history.append(balance)
        print(f"입금후 잔액 |{balance}|원")
    elif select==2:
        print(f"출금전 잔액 |{balance}|원")
        withdraw()
        history.append(balance)
    elif select==3:
        show()
    elif select==4:
        print("이용해주셔서 감사합니다")
        break
# ________________________________
# print(balance)
# amount=int(input())
# balance+=amount
# print(balance)