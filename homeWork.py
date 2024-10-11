

class CarPowerTrain():
    def __init__(self,engine,transMission,driveingMethod):
        self.engine=engine
        self.transmission=transMission
        self.driveingMethod=driveingMethod
    # 선택된 엔진의 타입
    def selectEngine(self,typeNum):
        if typeNum==1:
            print("1998 cc")
        else:
            print("it`s not our engin")
    def selectFuelType(self,typeNum):
        fuelTypeList=["diesel","gasoline","lpg","electricity"]
        if len(fuelTypeList)>=typeNum and 0 < typeNum:
            print("fuelType:",fuelTypeList[typeNum-1])
        else:
            print("lt`s not found")
    def selectTransmissionType(self,typeNum):
        transmissionTypeList=["auto","semiAuto","manual"]
        if len(transmissionTypeList)>=typeNum and 0 < typeNum:
            print("transmissionType:",transmissionTypeList[typeNum-1])
        else:
            print("lt`s not found")
    def selectDriveMetod(self,typeNum):
        driveMethodList=["AWD","FWD","RWD"]
        if len(driveMethodList)>=typeNum and 0 < typeNum:
            print("driveMethod:",driveMethodList[typeNum-1])
        else:
            print("lt`s not found")
            
class CarExterior():
    def __init__(self,color,headLight,wheel):
        self.color=color
        self.headLight=headLight
        self.wheel=wheel

    def selectWheelSize(self,typeNum):#휠사이즈 선택 
        inchList=[16,17,18,19,20,21,22,23]
        if len(inchList)>=typeNum and 0 < typeNum:
            print(inchList[typeNum-1],"inch")
        else:
            print("lt`s not found")
    def selectExtreiorColor(self,typeNum):#외장재 색 선택
        exteriorColorList=["red","yellow","white","black","gray","silver","navy"]
        if len(exteriorColorList)>=typeNum and 0 < typeNum:
            print(exteriorColorList[typeNum-1],"color")
        else:
            print("lt`s not found")
    def selectHeadLightsType(self,typeNum):
        headLightsTypeList=["bulbe","LED","HID"]
        if len(headLightsTypeList)>=typeNum and 0 < typeNum:
            print("headLightsType:",headLightsTypeList[typeNum-1])
        else:
            print("lt`s not found")
        
class CarInterior():
    def __init__(self,seats,multiMedia):
        self.seats=seats
        self.multMedia=multiMedia
        
    def selectIntreiorColor(self,typeNum):#내장재 색
        interiorColorList=["red","white","black","navy"]
        if len(interiorColorList)>=typeNum and 0 < typeNum:
            print(interiorColorList[typeNum-1],"color")
        else:
            print("lt`s not found")

class CarInfo:
    def __init__(self,carInterior,carExterior,carPowerTrain,price):
            self.carInterior=carInterior
            self.carExterior=carExterior
            self.carPowerTrain=carPowerTrain
            self.price=price
    def getCarinterior(self):
        return self.carInterior     
    def getCarExterior(self):
        return self.carExterior
    def getPowerTrain(self):
        return self.carPowerTrain
    def getPrice(self):
        return self.price
    def setCarExterior(self,carExterior):
        self.carExterior=carExterior
    def setCarinterior(self,carInterior):
        self.carInterior=carInterior
    def setCarPowerTrain(self,carPowerTrain):
        self.carPowerTrain=carPowerTrain
    def setPrice(self,price):
        self.price=price    
            

# car=CarInfo(1,2,3,4,5,6,7)
# car.selectEngine(1)
# car.selectWheelSize(6)
# car.selectExtreiorColor(4)
# car.selectIntreiorColor(2)
# car.selectHeadLightsType(6)
# car.selectFuelType(4)
# car.selectDriveMethod(3)
# car.selectTransmissionType(3)

# print(car.exterior,car.interior,car.powerTrain,car.headLight,car.wheel,car.seats,car.multMedia)



        
    