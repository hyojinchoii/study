
# 사용자 정의함수

# 형식)
# def 함수 ([인수])
# 실행문
# return 값

# dataset = list(range(1,6))
# print(dataset)
#
# # 방법1
#
# import statistics
# print('평균=',statistics.mean(dataset))
# print('중위수=',statistics.median(dataset))
# print('표준분산=',variance(dataset))
# print('표준편차=',stdev(dataset))
#
# # 인수가 없는 함수
#
# def userfunc():
#     print('인수가 없는 함수')
#     print(userfunc1)
#
#
# # return 있는 함수
# def userfunc3 (x,y):
#     print('userfunc3')
#     tot = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#
#     return tot,sub, mul, div
#
# # # 실인수 : 키보드 입력
# # x = int(input ('x 입력: '))
# # y = int(input ('y 입력 : '))
# #
# # t, s, m, d = userfunc3(x, y)
# # print('tot = ', t)
# # print('tot = ', s)
# # print('tot = ', m)
# # print('tot = ', d)
#
# # i_list = [10, 20, 30, 40]
# #
# # def pluslist (i_list):
# #     print(i_list)
# #     new_list = []
# #     for no in i_list:
# #         new_list.append(no+8)
# #     return new_list
# #
# # plus_list = pluslist(i_list)
# # print(plus_list)
#
# # 가변인수: 한개 가인수로 여러개의 실인수를 받을 수 있는 인수
# # 형식) def 함수면 (*인수)
#
# # def func1(name,grade, *subject):
# #     print(name)
# #     print(grade)
# #     print(subject)
# #
# # func1 ("아이유","1학년","째즈","발라드","팝","트로트")
#
# from statistics import mean, variance, stdev
#
# def statics( type, *data):
#     if type == 'avg':
#         return mean(data)
#     elif type == 'var':
#         return variance(data)
#     elif type == 'std':
#         return stdev(data)
#     else :
#         return "type err"
# print ('avg=', statics(('avg', 1,2,3,4,5,6)))
# print ('var=', statics(('avg', 1,2,3,4,5,6)))
# print ('std=', statics(('avg', 1,2,3,4,5,6)))
#
# # 사전형 가변 인수
# def emp_func(name, age,**other):
#     print(name)
#     print(age)
#     print(other)
#
# emp_func('초','22',a='a',b='b',c='c')
#
# # import random
#
# def coin(n):
#     result = []
#     for i in range(n):
#         r = random.randint(0,1)
#         if(r == 1):
#             result.append(1)
#         else:
#             result.append(0)
#         return result
#
#     print(coin(10))
#
# def montaCoin(n):
#     coin_set = coin(15)
#     print('합계:', sum(coin_set))
#     print('통계:', sum(coin_set)/n)
#     return sum (coin_set)/n
#
# print(montaCoin(30))
# print(montaCoin(300))
# print(montaCoin(3000))
# print(montaCoin(300000))
#
#
# # lamda 함수 - 축약함수
#
# # 1. 일반함수
#
# def Adder(x,y)
#     add = x + y
#     return add
#
# print ('add=', Adder(10,20))
# print('add=',(lamda x,y : x+y_)(10,20))

# 디폴트인수

# def sayhello(name,msg = "반갑습니다"):
# #     print("안녕",name + "," + msg)
# #
# # sayhello('하하','재미없어')
#
#
# # 람다에서 가변 인수 사용
#
# calc = lambda dan, su : dan * su
# print('price=', calc(2500,5))
#
# calc2 = lambda dan, *su, **product : print(dan,su,product)
# calc2(10000, 3, 5, a = 2500, b = 3000)
#
# # scope: 전역변수/지역변수
# # 전역변수: 전 지역 사용
# # 지역변수: 함수 or 블럭 (if, while, for) 사용
#
# def local_func(x):
# #     x +=50
# #     return x
# #
# #
# # print(local_func(1))
# #
# # y= 0
# # def local_func():
# #     global y
# #     y +=50
# #
# # print('y:',y)
# # local_func()
# # print('y:',y)
# # local_func()
# # print('y:',y)
# #
# # # 졸려용
# #
# # data = [1, 3, 5, 7, 9]
# # tot = 0
# #
# # def calc_func(data):
# #     global tot
# #     tot = sum(data)
# #     return tot
# #
# # print(tot)
# # calc_func(data)
# # print(tot)
# # calc_func(data)
# # print(tot)
#
#
# # 중첩함수 (nested function) - 내수함수를 외부함수 내에서 호출
#
# def outfunc(txt):
#     def innerfunc():
#         print(txt+"me-long")
#
#     innerfunc()
# outfunc("하하")
#
# #  중첩함수 - 외부함수 리턴값으로 내부함수 지정
#
# def a():
#     print('a함수')
#     def b():
#         print('b함수')
#     return b
#
# z = a()
# z()
#
# data = list(range(1, 101))
#
# def calc_data(data):
#     # 합계 inner 함수
#
#     def tot():
#         tot_val = sum(data)
#         return tot_val
#
#     # 평균 inner 함수
#     def avg(tot_val):
#         avg_val = tot_val/ len(data)
#         return avg_val
#     return tot, avg
#
# total, avgrage = calc_data(data)
# tot_val = total()
# print('total',tot_val)
#
# avg_val = avgrage(tot_val)
# print('total',tot_val)

# getter, setter 에 대한 개념
# getter 값을 가져오는 역할, setter 값을 지정하는 역할을 하는 함수

# 래퍼함수

def wrap(func):
    def decorated():
        print("hi")

        func()
        print('bye')
    return decorated

@wrap
def hello():
    print('아이유')

hello()

