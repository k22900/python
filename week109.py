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
        super().__init__()
        self.volume_Level=50
        
    def power_on(self):
        self.__battery = 100
        print("전원이 켜짐니다")

    def power_off(self):
        self.__battery = 0
        print("전원이 꺼짐니다")    
        
    def volume_up(self):
        pass
    
    def volume_down(self):
        pass
    
    def base_mod(self):
        pass
    
    def Surround_mod(self):
        pass
    
Speaker("SONY")