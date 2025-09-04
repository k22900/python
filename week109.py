# 머신 (엄마) -> 전원 킴, 전원 끔 (추상 메서드..!), 빠때리
#
# 스피커 : 전원 킴, 전원 끔, 볼륨 업, 볼륨 다운, 베이스 모드 서라운드 모드,
# 기능 조작하면 빠때리가 10씩 감소
# 빠때리가 0 이되면, 전원이 꺼져
# 전원 다시키면, 바때리 100
from abc import ABC, abstractmethod

# 공통 상위 클래스

class Machine(ABC):

    def __init__(self):
        self.__is_on = False
        self.__battery = 0
        
    def is_on(self):
        return self.is_on

    def battery(self):
        return self.battery

    @abstractmethod  # 하위 클래스에서 구현해라, 야 이거 있어야하는데 니네들이 해라
    def power_on(self):
        '''전원 켜기 : 하위에서 구현할 것 '''

    @abstractmethod
    def power_off(self):
        '''전원 켜기 : 하위에서 구현할 것 '''

# abstract method 하위에서 정의 해줘야해

# 스피커 : 전원 킴, 전원 끔, 볼륨 업, 볼륨 다운, 베이스 모드 서라운드 모드,
# 기능 조작하면 빠때리가 10씩 감소
# 빠때리가 0 이되면, 전원이 꺼져
# 전원 다시키면, 바때리 100
class Speaker(Machine):
    def __init__(self, brand):
        self.brand=brand
        self.__volume_Level=50
        self.mod_status=False #기본값:base_mod
        
    def power_on(self):
        self.is_on=True
        self.__battery = 430
        print("전원이 켜짐니다")

    def power_off(self):
        self.is_on=False
        self.__battery = 0
        print("전원이 꺼짐니다")    
        
    def volume_up(self):
        if self.__battery<=0:
            print("배터리가 부족합니다")
            return None
        self.__battery-=10
        
        if self.is_on == False:
            print("현재 전원이 꺼져있습니다")
            return None
        self.__volume_Level=min(self.__volume_Level+5,100)
        print(f"현재 음량: {self.__volume_Level}\n현재 배터리 잔량은 {self.__battery}입니다")
        pass
    
    def volume_down(self):
        if self.__battery<=0:
            print("배터리가 부족합니다")
            return None
        self.__battery-=10
        
        if self.is_on == False:
            print("현재 전원이 꺼져있습니다")
            return None
        self.__volume_Level=max(self.__volume_Level-5,0)
        print(f"현재 음량: {self.__volume_Level} \n현재 배터리 잔량은 {self.__battery}입니다")
        pass
    
    def base_mod(self):
        if self.__battery<=0:
            print("배터리가 부족합니다")
            return None
        self.__battery-=10
        
        if self.is_on == False:
            print("현재 전원이 꺼져있습니다")
            return None
        if self.mod_status==False:
            print(f"이미 음향효과 타입이 베이스 입니다 \n현재 배터리 잔량은 {self.__battery}입니다")
            return None
        self.mod_status=False
        print(f"음향효과: base \n현재 배터리 잔량은 {self.__battery}입니다")
    
    def Surround_mod(self):
        if self.__battery<=0:
            print("배터리가 부족합니다")
            return None
        self.__battery-=10
        
        if self.is_on == False:
            print("현재 전원이 꺼져있습니다")
            return None
        if self.mod_status==True:
            print(f"이미 음향효과 타입이 서라운드 입니다 \n현재 배터리 잔량은 {self.__battery}입니다")
            return None
        self.mod_status=True
        print(f"음향효과: surround \n현재 배터리 잔량은 {self.__battery}입니다")
    def battery_charge(self):
        self.__battery=100
    
sp=Speaker("SONY")
sp.power_on()
sp.volume_down()
for _ in range(15):
    sp.volume_down()
for _ in range(25):
    sp.volume_up()
sp.Surround_mod()
sp.Surround_mod()
sp.base_mod()
sp.base_mod()