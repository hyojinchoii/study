# 문제 1
#
su = 5
print(su)
print(id(su))

dan = 800
print(dan)
print(id(dan))

a = 5
b = 800
print("5*800", a * b)

# 문제 2
x = 2
y = 2.5 * x ** 2 + 3.3 * x + 6
print(int(y))

# 문제 3
number1 = input("지방의 그램을 입력하세요")
number2 = input("탄수화물의 그램을 입력하세요")
number3 = input("단백질의 그램을 입력하세요")
print(int(number1) * 9 + int(number2) * 4 + int(number3) * 4)

# 문제4
word1 = "Korea"
word2 = "Baseball"
word3 = "Orag"
print(word1.count(1))

print("%05d" % 876)
