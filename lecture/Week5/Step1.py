
def student():
 pass

class student:
    name = ''
    major = ''
    grade = ''
    subject = dict()

#     생성자: 기본적으로 자동 생성
    def __init__(self,name,major,grade):
        self.name = name
        self.major = major
        self.grade = grade
        self.subject = dict()

#   method 함수
#   값을 지정하는 set 함수
    def setname(self,t_name):
        self.name = t_name

    def setmajor(self,major):
        self.major = major

    def setgrade(self,grade):
        self.grade = grade

    def setsubject(self, key, value):
        self.subject[key] = value
        # self.subject.__setitem__(key,value) 매직함수



    # get 함수

    def getname(self):
        return self.name

    def display(self):
        print("학생명:{}, 학과:{}, 학년:{}".format(self.name,self.major,self.grade))

    def getsubject(self):
        for i in self.subject:
            print(i,end = '')

    # 인스턴스 생성

# st1 = student()
# st1.setname("나꼼꼼")
# st1.setmajor("컴퓨터공학과")
# st1.setgrade("1학년")
# print(st1.getname())
#
# st1 = student()
# st1.setname("왕꼼꼼")
# st2.display()

st3 = student('아이유','연예방송과','2학년')
st3.display()

st4 = student('호호','간호학과','4학년')
st4.display()

st5 = student('조수미','성악과','4학년')
st5.setsubject('소프라노',100)
st5.setsubject('바리톤',100)
st5.setsubject('째즈',100)
st5.setsubject('팝',100)
st5.display()
st5.getsubject()

st6 = student('전지현','연기과','4학년')
st6.setsubject('개그',100)
st6.setsubject('멜로',100)
st6.setsubject('로맨스',100)
st6.setsubject('노래',100)
st6.display()
st6.getsubject()