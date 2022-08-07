# for _ in range(1, 101, 3):
#     print(_)
# _ 임의의 숫자로 변수값 주기

# for _ in range (101,1,3):
#     print(_)

# hap= 0
#     for _ in range(1,101):
#     if _ % 5 == 0 :
#     hap += _
# print('hap =%d' %(hap))

#  1 ~100 수 중 짝수, 홀수의 합계 구하기

# for _ in range (1, 101):
#     if _ % 2 == 0:
#         evensum += _
#     else:
#         oddsum += _
#         print('짝수의 합: %d, 홀수의 합 : %d' %(evensum, oddsum))

# 구구단 단 찍기
# dan = int(input("확인 하려는 구구단 단을 입력하세요"))
# for i in range(1, 10):
#     print("%d x %d = %d" %(dan,i,dan*i))

# 외부 반복문
# for dan in range(2, 10):
#
# # 내부 반복문
# for i in range(1, 10):
# print("%d x %d = %d" %(dan,i,dan*i), end="\ｔ")

#두개의　주사위의　두눈의　합이　６이　되는　모든　경우의　수를　출력하시요

#  1~ 100의 합을 구하되, 3의 배수를 제외하고 더하기

# hap, i = 0, 0
# for i in range(1,101)
#     if i % 3 ==0 :
#         continue
#         evensum += i

# 비밀번호 확인
#  7895의 패스워드를  7895일때만 허용, 그렇지 않을때는 비허용

# while True:
#     password = (int(input("비밀번호를 입력하세요")))
#
#     if password == 7895 :
#         print("환영합니다 ")
#         break
#     else:
#         print("잘못된 비밀번호입니다")
#         continue

# 랜덤함수 추출하기
# import random
# print(random.random())
# print(int(random.random()*45))
print(random.randrange(1,46))asdsda