# N1 = 10
# N2 = 20
# result = false
#
# #  같은지 비교 ==
# result = N1 == N2
# print(result)
#
# #  서로 다른지 비교 !=
# result = N1 != N2
# print(result)
#
# # 논리연산자 ; 논리곱, 논리합, 부정
#
# # 논리연산자 and
#
# result = N1 >=10 AND N2 < 10
# print(result)
#
# # 논리연산자 OR
#
# # 논리연산자 not
# result = not (N1 >= 10)
# print(result)
#
# # 대입연산자 = , (a,b), 패킹 할당
#
# # 변수 선언 후, 초기값 대입
# v1, v2, v3 =10, 20, 30
# print(v1,v2,v3)
#
# # 변수 교체
# v2, v1 = v1, v2
# print( v1)
# print( v2)
#
# # 패킹할당 - 묶음으로 할당을 하겠다. 표현 기호는 *
# lst = [1, 2, 3, 4, 5]
#
#
# # 복합연상자
# x=1000
# print("초깃값 x=", x)
#
# x+=2;
# print("x+=2 후의 x=", x)
#
# x-=2;
# print("x-=2 후의 x=", x)
#
# i=5
# print(i)
# j = i
# print(id(j)
#
# i=10
# print(j)
#
# # 숫자 입력하기
# unmber = input("숫자를 입력하세요")
# print(unmber)
#
# number1 = input("첫번째 숫자를 입력하세요")
# number2 = input("두번째 숫자를 입력하세요")
# print(int(number1) > int(number2))
#
# number1 = input("분자를 입력하시오")
# number2 = input("분모를 입력하시오")
# print(div(number1)/(number2))
# print(div2(number1)/(number2))
#
# # help(print)
# # help(내장함수)
#
# print("010","4564","1231",sep="-",)
#
# str1 = "파이썬 기능 짱"
# print(str1[2])
# print(str1*4)
#
# # 내장함수(len)- 문자길이
# print(len(str1))
#
# # 내장함수 (type) - data type 알아보기
# print(type(str1))
#
# # format 내장함수
# print( format(3.14159, '8.3f'))
#
# print( format(12345, '10d'))
# print( format(12345, '3,d'))
# print( format(123456789, '3,d'))
#
# #  선언 2번째 방법
# num1  , num2  =10,20
#
# # 선언 3번째 방법
# num = 10; num2 =20
# tot = num1 + num2
#
# # print( num1, "+", num2, "=" , num1+ num2)
# print("10+20=%d", %tot)
# print("%d+%d=%d" %(num1,num2,tot))
#
# # 문자열 슬라이싱
# str2 = "너무 좋습니다."
# print(str2[3:5])