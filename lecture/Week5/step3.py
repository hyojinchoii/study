
# 부모 클라스
class flight:
    def fly(self):
        print('날다, fly 원형 메서드')

        # 자식 클라스
class airplane(flight) :

        # 함수 재정의
    def fly (self):
        print('비행기가 날다.')

class bird(flight):
    def fly(self):
        print('새가 날다.')

class paperairplane(flight):
    def fly(self):
        print('종이 비행기가 날다.')

flight = flight()
air = airplane()
bird = bird()
paper= paperairplane()

