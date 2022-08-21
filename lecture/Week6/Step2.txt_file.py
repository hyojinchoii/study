# 텍스트 파일 입출력
# 데이터 입출력 시 반드시 예외 처리한다


# open (file = , mode = , encoding = )
# 현재 시스템의 정보를 가져오는 모듈

import os
print(os.getcwd())
# #
# # # alt + shift + e : 영역실행
# #
def ex1():
    f = open('lecture/Week6/food_e.txt','r')
    content = f.read()
    print(content)
ex1()
#
# # 한줄 읽어오기
#
def ex2():
    f = open('lecture/Week6/food_e.txt', 'r')
    line_data = f. readline()
    print(line_data)
    print(type(line_data))
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

    f = open ('lecture/week6/food_e.txt', 'r')
    for i in range(10):
        line_data = f.readline()
        if line_data == 'pizza':
            print('피자 찾음', line_data)
        else:
            print('못찾음',line_data)


# # 한글파일 읽어오기
#
def ex3():
    f = open('C:\최효진\lecture\Week6\Step2\food_k.txt', 'r', encoding = "utf8")
    content = f.read()
    print(content)
    print(type(content))

# 파일 쓰기

def ex4():

    try:
        str = '고양이, 코끼리, 사자, 호랑이, 강아지, 햄스터, 박쥐, 너구리'
        w_list = list(str.split(''))
        print(w_list)

        f = open('C:\최효진\lecture\Week6\animal.txt', 'w', encoding="utf8")
        for w in w_list:
            f.write(w+'\n')
        f.close()

    except Exception as e:
        print('예외발생', e)
    finally:
        # f.close()
        pass

# 파일열기 with을 사용하여 열기 (close가 필요 없음)
def ex5():
    with open('lecture/Week6/food_E.txt','r',encoding= "utf8") as f :
        # 여러줄 한번에 읽어오기
        content_list = f.readlines()
        print(type(content_list))
        print('문단수:',len(content_list))

def ex6():
    with open('lecture/Week6/food_k.txt','r',encoding= "utf8") as f :
        contents = f.read()
        print('글자수:', len(contents))

