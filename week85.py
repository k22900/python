# import pandas
# import matplotlib.pyplot as pl
# numpy.
# 단어집을 어떻게 담지?
# ->
# 배열로한번에[["append",["추가하다"]],["remove",["제거하다"]],["install",["설치하다"]],["nuinstall",["제거하다"]],["source",["출처","근원"]]]??
import numpy as np
import tkinter as tk
# 초기정보

# 메인  ( 계속 반복 )
# - 단어를 보여주는 기능
# - 정답을 입력받는 기능
# - 정답과 입력을 비교 후 정답인지 알려주는 기능

# 종료

wordDictionary = [["append", ['추가하다']],
                  ["remove", ['제거하다']],
                  ["install", ['설치하다']],
                  ["uninstall", ['제거하다']],
                  ["source", ['출처', '근원']],
                  ["continue", ['계속']],
                  ["immutable", ['불변']],
                  ["mutable", ['가변']]
                  ]

# 뭘하는 함수 인지
# @Param :
# @Return ㅣ


def addWordMeaning():
    wordMeaning = []
    isRunning = True

    while isRunning:
        print("위에서 입력한 단어의 의미를 적어주세요.")
        print("단어의 의미가 2개이상일경우 지금 물음에는 1개만 적어주세요")
        meaning = input("입력 : ")
        st = True

        print(f"입력하신 의미가 {meaning}가 맞습니까?")
        print("맞으면 yes 아니면 no를 입력해주세요")
        temp = input("입력 : ")

        if temp == "yes":
            wordMeaning.append(meaning)
            isRunning = False
            continue
        elif temp == "no":
            continue
    running = True

    while True:

        print("단어의 의미를 더 입력 하시겠습니까?")
        print("맞으면 yes 아니면 no를 입력해주세요")
        temp = input("입력 : ")

        if temp == "yes":
            while running:

                print("추가로 입력하실 의미 1개를 적어주세요")
                meaning = input("입력 : ")

                print(f"입력하신 의미가 {meaning}가 맞습니까?")
                print("맞으면 yes 아니면 no를 입력해주세요")
                temp = input("입력 : ")

                if temp == "yes":
                    wordMeaning.append(meaning)
                    break
                elif temp == "no":
                    continue

        elif temp == "no":
            return wordMeaning


def addWords(words):
    isRunning = True

    while isRunning:
        printTemplate("추가하려는 영어단어 1개만 적어 주세요")
        word = input("입력 : ")
        wordMeaning = addWordMeaning()
        words.append([word, wordMeaning])
        print("단어를 더추가 하시겠습니까?")
        print("맞으면 yes 아니면 no 를 입력해주세요")
        check = input("입력 : ")
        if check == "yes":
            continue
        elif check == "no":
            return words


# <~~~~~~~~~~~>

#
# '    계속'

# '1111계속'
# '계속'

#  단어를 썪어,,
#
def judgment(questionAnswers, inputAnswer):
    for ans in questionAnswers[1]:
        if ans == inputAnswer:
            return True
    return False


def showWord(word):
    # 단어를 보여준다.
    question = word[0]
    questionAnswers = word[1]
    print(question)


def inputAnswer():
    # 답을 입력받는다 .
    return input("입력 : ").strip()  # .strip() 양끝 공백 제거


def playTest(words):
    printTemplate("         테스트 모드 시작")
    np.random.shuffle(words)
    while words:
        word = words[-1]

        # 단어를 보여준다.
        showWord(word)

        # 답을 입력받는다 .
        clientAnswer = inputAnswer()
        # 정답인지 아닌지 판단한다.
        result=judgment(word,clientAnswer)
        if result:
            printTemplate("              정답입니다")
            words.pop()
            continue
        else:
            printTemplate("             오답입니다")
            continue
    # print(len(words))


def checkWordDictionary(words):  # 암기 사전에 등록된 단어확인
    lenth = len(words)
    print(f"현제 등록된 단어는 {lenth}개 이며 등록된 단어들은")
    for str in words:
        print(str)
    print("입니다")
    while True:
        printTemplate("다시 메뉴로 돌아가시려면 yes를 입력해주세요")
        command = input("입력 : ")
        if command == "yes":
            return
        else:
            printTemplate("잘못 입력 하셨습니다 다시 입력해주세요")
            continue


def runProgram(wordDictionary):
    isRunning = True
    while isRunning:
        showNotice()
        command = input("키워드 입력 : ")

        if command == "exit":
            printTemplate("     프로그램을 종료합니다")
            isRunning = False
            continue

        elif command == "test":
            command = playTest(wordDictionary)  # 단어 테스트 실행

        elif command == "add":
            wordDictionary = addWords(wordDictionary)

        elif command == "check":
            checkWordDictionary(wordDictionary)

        else:
            printTemplate(f" {command} : 키워드는 유효하지않습니다.")


def showNotice():
    
    printTemplate("============= 단어 암기 ============= ")
    print("사용할 기능에 해당하는 키워드를 입력해주세요.")
    print("test - 문제 풀기 ")
    print("add - 암기할 단어를 추가 ")
    print("check - 현재 등록된 단어를 확인 ")
    print("exit - 프로그램을 종료 ")


def printTemplate(string):
    print("===================================== ")
    print(string)
    print("===================================== ")


runProgram(wordDictionary)

import tkinter