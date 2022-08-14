class permanent(employee):

    def __init__(self,name,hire_type):
        self.name = name
        self.hire_type = hire_type
        self.salary = 0

   def pay_calc(self):
         print('이름: {}, 고용형태 :{}, 급여:{}'.format(self.name,self.hire_type, self.salary)

class temporary(employee)

    def __init__(self,name,base, hour):
        super().init__(self,name,'임시직')
        self.salary = base * hour

emp_list = []
seq = 0
while seq < 4:
    seq += 1
    inputtype = input("고용형태를 입력하세요. 정규직:p, 임시직:t")
     if inputtype  == 'p' or emptype == 'P' :
         name = input('이름: ')
         base = int(input('기본급: '))
         bonus = int(input('상여급 :'))
         p = permanent(name,base,bonus)
         p.pay_calc()
    else  inputtype   == 't' or emptype == 'T' :
         name = input('이름: ')
         base = int(input('기본급: '))
         hour = int(input('시간: '))
         t = temporary(name,base,hour)
         t.pay_calc()
print(emp_list)