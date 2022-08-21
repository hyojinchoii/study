# 예외 상황에 어떻게 처리하는지

def ex1():
    x = [10,20,30,14,'몰라',51]

    print('프로그램 시작')
    for i in x:
        y = i**2
        print(y)

    print('프로그램 끝')

# 예외처리 1
def ex2():
    x = [10, 20, 30, 14, '몰라', 51]

    print('프로그램 시작')
    try:
        for i in x:
            y = i ** 2
            print(y)

    except :
        print ('오류발생')

    print('프로그램 끝')

# 예외처리 2
def ex2():
    x = [10, 20, 30, 14, '몰라', 51]

    print('프로그램 시작')
    for i in x:
        try:
            y = i ** 2
            print(y)

    except typeError as e :
        print ('typeError 오류발생: 자료형 확인', e)

    print('프로그램 끝')

import builtins
print(dir(builtins))

def ex4():
    for i in range(10)
        try:
           print (10/i)
        except ZeroDivisionError:
            print("Not divided by 0")
            print(e)
        # 예외상황과 상관없이 무조건 실행
        finally:
            print('프로그램 종료')

def ex5():
    try:
        div =1000/2.53
        print('div = %5.2f' % (div))
        div = 1000/ 0
        f = open ('c:\\a.txt')
        num = int(input('숫자입력 : '))
        print('num = ', num)

    except ZeroDivisionError as e :
        print('오류 정보 1: ', e)
    except FileNotFoundError as e :
        print('오류 정보 2: ', e)
    except Exception as e :
        print('오류 정보 3: ', e)
    finally:
        print('모든 예외상황 확인')


# raise 예외 발생
# 미리 알아야 할 예외 정보가 조건에 만족하지 않을 경우, 예외를 발생시키는 구문이다

while True:
    value = input ('변환할 정수 값을 입력해 주세요')
    for digit in value :
        if digit not in "0123456789" :
            raise ValueError("숫자값만 입력 가능")
        print ('변화된 정수값: ', int(value))


