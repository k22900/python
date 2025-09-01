class Vehicle:
    def __init__(self,color,year,engine):
        self.color=color
        self.__year=year
        self.engine=engine
        self.__speed=0
        self.__ready=False
        
    def getInfo(self):
        print(f"생산년도 : {self.__year}")
        print(f"엔진 : {self.engine}")
        print(f"색상 : {self.color}")
    
    def turnOn(self):
        self.__ready=True
        print("시동이 켜졌습니다 안전운전 하세요")
        
            
    def turnOff(self):
        self.__ready=False
        print("시동이 꺼졌습니다 안녕히 가세요")
        
            
    def accelerate(self) -> None:
        if self.__ready==False:
            print("시동이 꺼져있습니다")
            return 
        self.__speed=min(self.__speed+10,100)
        print(self.__speed)
        
    
    def decelerate(self) -> None:
        if self.__ready==False:
            print("시동이 꺼져있습니다")
            return
        self.__speed=max(self.__speed-10,0)
        print(self.__speed)
        
    
        
        
# class HevCar(Car):
#     def __init__(self,color,year,engine):
#         super().__init__(color,year,engine)
        
        
# class EvCar(Car):
#     def __init__(self,color,year,engine):
#         super().__init__(color,year,engine)
 
kCar=Vehicle("red",2022,1.6)
kCar.accelerate()
kCar.turnOn()
kCar.decelerate()
kCar.accelerate()
for _ in range(12):
    kCar.accelerate()
for _ in range(12):
    kCar.decelerate()


