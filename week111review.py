
from enum import Enum
"""
student 객체,
이름 , 점수, grade (enum)
생성자로 이름, 점수 -> grade 연산

학생의 getInfo -> 이름 , 점수, grade

100 ~ 95 -> A+ Grade
95 ~ 90 -> A0 Grade
90 ~ 85 -> A- Grade
+ 시험 : 국어 , 수학 , 영어 -> grade 있어
"""


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

    def __init__(self, symbol, min_score):
        self.symbol = symbol
        self.min_score = min_score

    @classmethod  # get_grade_by_score가 클래스 자체를 호출 할 수 있는 메서드가 돼
    def get_grade_by_score(cls, score):
        for grade in cls:
            # print(grade.min_score,grade.symbol)
            if score >= grade.min_score:
                # print(*cls)
                print(grade.symbol)
                return grade.symbol
        # return cls.F.symbol


class Student:
    '''학생 정보와 성적을 관리하는 클래스'''

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = min(score, 100)
        self.grade = Grade.get_grade_by_score(self.score)

    def get_info(self):
        print(f"{self.name} | {self.score} | {self.grade}")


class Exam:
    def __init__(self, year: int, semster: int, subject: str):
        self.year = year
        self.semster = semster
        self.subject = subject


jimin = Student("지민", 0)

jimin.get_info()
