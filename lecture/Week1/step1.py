a=100
print(a)
print (id(a))

a=200
print(a)
print(id(a))

break_a="안녕"

# 한줄주석
# 2진수를 8진수로 바꿔보고 싶다
"""아아아아아아아아아악 살려줘
무슨 말인지 모르겠어 살려주세요"""

f=bin(42)
print(f)
print(oct(f))

b=bin(25)
print (b)
print(int(b,2))

#2진수 -> 10진수 -> 8진수
f=bin(42)
print(f)
print(oct(int(f,2)))

# 2진수 -> 10진수 -> 16진수
g=bin(34)
print(g)
print(hex(int(g,2)))

# 변수선언
# 실수형
var1=120.4

# 논리형
var2=true
print(var2)

#문자열
VAR3= "python good"


# 연산자 구하기

x=7
y=4
print("7+4",x+y)
print("7-4",x-y)
print("7*4",x*y)
print("7/4",x/y)
print("7%4",x%y)

i = int(10.5)
j = int(20.42)
add= i+j
print(add)

# int 는 실수 ->정수
#  float 정수 -> 실수

# 제곱연산
str ='10'
print(str+int(str**3))


