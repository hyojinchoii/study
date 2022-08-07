# 무한반복 돌리기

# import random
# lotto_no = []
# lotto_ctn = 0
# while True:
#     lotto_no.append(random.randrange(1,46))
#     if lotto in lotto_no:
#
#         lotto_ctn+=1
#
#     if lotto_cnt == 6:
#         break
# print(lotto_no)

#  리스트 공부하기

a= [1,2,3,4,5]
b = []
for num in a :
    print (num , end="\t")
    b.append(num*3)

print(b)

# 리스트 내 반복문 포함하기

a= [1,2,3,4,5,6,7]
result = [num*3 for num in a]
print(result)

# 리스트 내 조건 포함하기

a= [1,2,3,4,5]
b = []
for num in a :
    if num %2 ==0 :
        b.append(num)
print (b)

# 리스트 내에 반복문 조건문 포함하기

a= [1,2,3,4,5,6,7]
b= [num for num in a if num %2 == 0]
print (b)

#  1~100 사이에 수 중에 2의 배수를 리스트에 담기

a = range(1,101)
b = [ ]
for num in a :
    if num % 2 ==0 :
        b.append(num)
print (b)

#  다른 방법으로 2의 배수 리스트에 담기 - 1

a = range(1,101)
b = [num for num in a if num %2 == 0]
print (b)

#  다른 방법으로 2의 배수 리스트에 담기 - 2

list = [ i for i in range(1,101) if num %2 ==0 and num %5 ==0]
print(list)

# 별 찍기 (왼정렬, 오른 정렬)

List(str(*),+= 1)

cnt = int(input("반복 횟수를 입력하세요"))
star = "*"
for i in range(0,cnt,1) :
    print("%{0}s".format(cnt)%star)
    star += "*"

# 리스트에 삽입하기
list=["수박","바나나","홍시","코코넛"]
print(list)
list.append("키위")
print(list)
list.insert(2,"복숭아")
print(list)
list.remove("홍시")
print(list)
del list [0]
print(list)
list.pop()
print(list)
print(list.index("바나나"))

# 문자열 스트링

string="아이유 유재석 신동엽 송강 차은우"
member_list = [ ]
for i in string.split ():
    member_list.append(0)

print(member_list)

print ('올해의 MVP 후보 명단입니다. {}'.format(member_list))
choice_member = random.choices(member_list, k=2)
print('올해의 MVP 후보 명단입니다. {}'.format(choice_member))

print(len(list))

# 리스트

a = [1,2,3,4,5]
print(a)
print(type(a))
for i in a :
    print(a[0:i])

# 반대로 슬라이싱
a = [1,2,3,4,5]
print(a)
for i in a :
    print(a[i:])

# 중첩 list객체 생성
b= [10,20,a,5, true, '문자열']
print(b)

# 2차원 리스트
aa = [[1,2,3],[4,5,6],[7,8,9]]
print(aa)

# 2,6,8 추출하기
print (aa[0][1])
print (aa[1][2])
print (aa[2][1])

# 실습문제 만들기

a = range(0,60)
b = [num for num in a if num %3 == 0]
print (b[0:5])
print (b[5:10])
print (b[10:15])
print (b[15:20])

