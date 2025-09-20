from enum import Enum
# student 객체,
# 이름 , 점수, grade (enum)
# 생성자로 이름, 점수 -> grade 연산

# 학생의 getInfo -> 이름 , 점수, grade

# 100 ~ 95 -> A+ Grade
# 95 ~ 90 -> A0 Grade
# 90 ~ 85 -> A- Grade
# + 시험 : 국어 , 수학 , 영어 -> grade 있어

class Grade(Enum):
    A_P = ("A+", 95)
    A_Z = ("A0", 90)
    A_M = ("A-", 85)
    B_P = ("B+", 80)
    B_Z = ("B0", 75)
    B_M = ("B-", 70)
    C_P = ("C+", 65)
    C_Z = ("C0", 60)
    C_M = ("C-", 55)
    F = ("F", 0)
    
    def __init__(self,symbol,score):
        self.symbol=symbol
        self.min_score=score
    
    @classmethod
    def get_grade_by_score(cls,score):#cls가 어떤원리로 적용되는거지?
        score=max(score,0)
        for grade in cls:
            if score >= grade.min_score:
                print(grade.symbol)
                return grade.symbol
        return cls.F.symbol#끝까지 확인 않하나?
class Student:
    
    def __init__(self,name:str,score:int):    
        self.name = name
        self.score = min(score,100)
        self.grade = Grade.get_grade_by_score(self.score)
    
    def get_info(self):#간단한 프린트로 구현한 성적 등급조회
        print(f"{self.name} | {self.score} | {self.grade}")


jimin = Student("지민", 0)

jimin.get_info()