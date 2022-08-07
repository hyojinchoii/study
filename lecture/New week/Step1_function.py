
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

def sayhello(name,msg = "반갑습니다"):
    print("안녕",name + "," + msg)

sayhello('하하','재미없어')
