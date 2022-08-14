# 멤버 변수
cc = 0
door = 0
cartype = None

class car:
    cc = ''
    door = ''
    cartype = ''

    def __init__(self, cc, door, cartype):
        self.cc = cc
        self.door = door
        self.cartype = cartype

    def display(self):
        print("엔진:{}, 문짝_갯수:{}, 차type:{}".format(self.cc,self.door,self.cartype))


car1 = car('2000', '4', '승용차')
car1.display()

car2 = car('3000', '2', '스포츠카')
car2.display()