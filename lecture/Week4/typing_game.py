
import random

def getstarwordgame(cnt):

    wordlist = ["book","pencile","eraser","pen","pencile_case","bag"]

    i = 0
    while i < cnt:
        i += 1
        ai_choice = random.choice(wordlist)
        print("*문제",i)
        print(ai_choice)

        my_answer = input("")

        if ai_choice == my_answer:
            print("통과")
            i += 1
            ai_choice = random.choice(wordlist)

        else:
            print("다시 입력하세요")


