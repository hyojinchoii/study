# list의 나열

x = [1,2,3,4]
y =[1.5, 6.3]

z = x+y
print(z)

# 리스트의 확장
x.extend(y)
print(x)

# 리스트의 제곱 == 배열 복사

lst = [1,2,3,4]
result = lst * 2
print(result)

# 리스트 sort

result.sort(reverse = True)
print(result)

# 2차원 리스트의 확장
#101(2) 102(3)
#201(5) 202(3)
#301(2) 302(6)
#401(4) 402(7)
#501(1) 502(4)

# 각 층의 인구수와 빌라 전체의 거주 인구수를 구하시오
house = [ [2,3],[5,3],[2,6],[4,7], [1,4]]
layer_total = 0
total = 0

for floor in range(0,5):
    print(house[floor])
    for room in range(0,2):
        print('%중의 %호 거주 인구수 %d' %(floor+1,room,house[floor][room])
              total += house[floor][room]
              layer_total += house[floor][room]
    print('%d중의 거주 인구수 합계 %d' %(floor+1, layer_total))
print('파이썬빌라의 거주 인구수 합계 %d'%(total))



# 튜플

tt1=(10,20,30,40)
tt2=('a','b','c')
print(tt1+tt2)

#단일인수
t =10 ; t1 = (10, )
t= (10)

# 여러개 인수
t2 = (1,2,3,4,5,3)
print(t2[0],t2[1:4])

# 튜플을 리스트형으로 형변환
mTT = (10,20,30)

# 딕셔너리

items ={ "아메리카노":1500 , "라떼":4500, "밀크티": 2500, "레모네이드": 4500}
# print(type(items))
# print(items)
#
# print(items["아메리카노"])
# print(items.keys())
#
items["아메리카노"]= 2500
print(items)

# 삭제
del items["레모네이드"]
print(items)

# 아이템 추가하기
items ["미숫가루"] = 3000
print(items)

# 존재여부 검색
print("레모네이트" in items)

for k in items. keys():
    print(k)
for k in items. values():
    print(k)
for k in items. items():
    print(k)

    print("ㅋ"*9)

while True:
    print("메뉴:{0}".format(items)")
    order = input("주문하시겠습니까?")
    items = {"아메리카노": 1500, "라떼": 4500, "밀크티": 2500, "레모네이드": 4500}

    if order in items :
        print("네, 감사합니다. 가격은 {0}입니다.".format(items[order]))

    else:
        print("메뉴를 다시 확인해주세요")
        continue

