class Cat:
    # 메서드,멤버변수,생성자
    def __init__(self,catType,color):
        self.catType=catType
        self.color=color
    def sound(self):
        print("냥~")
        
    # 고양이가 내는 소리 의메서드 제작
#   생성된 객체를 인스터스라 하고
myCat=Cat("cl","black")
myCat.sound()
print(myCat.catType,myCat.color)
