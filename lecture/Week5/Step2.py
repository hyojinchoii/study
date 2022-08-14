# # 소멸자
#
# class multiply:
#     x = y = 0
#
#     def __del__(self):
#         del self.x
#         del self.y
#
# obj = multiply(10,20)
# print('곱셈',obj.mult())
#
#
# # 입출금 class 함수로 바꾸기
#
# blance = 0
# accname = ''
# accNo = None
#
#     # 생성자 : 초기화
#
#     def __init__(self,bal, name, no):
#         self.balace = bal
#         self.name = name
#         self.accNo = no
#
#     # 잔액확인
#
#     def getbalace(self):
#         priny("계좌:{}의 현재 잔액은 {}원입니다.".format(self.accNo,self.accname,self.balace))
#
#     def deposit(self,money):
#         # 마이너스 금액 걸러내기
#         if money < 0:
#             print('금액 확인 필수')
#         self.balance += money
#         print(format(money, "3,d") + "원이 입금되었습니다")
#
#
#     def withdraw(self,money):
#         if self.balance > money:
#             self.balace -= money
#         self.balance -= money
#         print(format(money,"3,d"),'원이 출금되었습니다.')
#         else:
#         print("잔액이 부족합니다.")
#         return
#
# acc1 = account(20000,'나공주', '0001')
# acc1.getbalance()
# acc1.deposit(500000)
# # acc1.getbalance(4000)
# # acc1.withdraw(50000)
# #
# # print(acc1.accName)
#
# # 상속
#
# class person(object):
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def about_me(self):
#         print("저의 이름은",self.name,"이고요, 나이는", str(self.age),"살이며,",self.gender,"입니다")
#
# person1 = person("아이유",30,'여자').about_me()
#
# class employee(person):
#     def __init__(self,name,age,gender,salary,hire_date):
#         super().__init__(name,age,gender)
#         self.salary = salary
#         self.hire_date = hire_date
#
#     def about_me(self):
#         super().about_me()
#         print("제 급여는",self.salary,"원이고, 제 입사일은",self.hire_date,"입니다.")
#
#     def pay_calc(self):
#         return self.salary
#
#     # employee1 = employee("아이유",30,'여자',50000000,'20090604').about_me()
#
# class permanent(employee):
#     def __init__(self,name,age,gender,salary,hire_date):
#         super().__init__(name,age,gender,salary,hire_date)
#
#
#     def pay_calc(self,bonus):
#         self.salary = self.salary  + bonus
#         print('총 수령액:',self.salary,"원 입니다.")
#
# class temporary(employee):
#     def __init__(self, name,age,gender,salary,hire_date):
#         super().__init__(name,age,gender,salary,hire_date)
#
#     def pay_calc(self,time):
#         self.salary = self.salary * time
#         print('총 수령액:',self.salary,"원 입니다.")
#
#
# p1 = permanent ("홍성동",40,"남자",2000000,"20010605")
# p1.about_me()
# p1.pay_calc(5)
#
# t1 = temporary("홍길동",30,"남자",10000,"20010605")
# t1.about_me()
# t1.pay_calc(5)


# 상속 예제 2

class parent:
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def display(self,name,job):
        print('name: {}, job : {}'.format(self.name, self.job))

    p1 = parent('홍길동','회사원')
    p1.display()

class children(parent):
    def __init__(self, name,job,gender):
        super().__int__(name,job)
        self.gender = gender

    def display(self):
        print('name: {}, job : {}','gender{}'.format(self.name,self.job,self.gender))

    chil1 = children("보라돌이","뚜비","나나")
    chil1.display()




