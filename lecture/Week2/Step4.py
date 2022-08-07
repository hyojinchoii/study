# 딕셔너리는 중복을 허용하지 않음
# list와 듀플은 중복을 허용

# set의 특징 : 순서 없음. 중복허용 불가

s= {1,3,5,3,1}
print(s)

# for d in s :
    # print(d, end ='')  1,3,5
s2 = {3, 6}

# 합집합
print(s.union(s2))

# 차집합
print(s.difference(s2))
# 교집합
print(s.intersection(s2))

s3 ={1,3,5}

#  7을 추가한다
s3.add(7)
print(s3)

#  대체한다
s3.update([5,'다섯'])
print(s3)

# 리스트는 중복 허용이지만, set형으로 바꿔서 중복 제거하기
sMenu = ["가","나","다","라","가","나"]

sMenu = set(sMenu)
print(sMenu)

# set을 다시 list로 바꾸기 - 중복허용
sMenu = list(sMenu)
print(sMenu)

# 함수

def sayhello():
    print('안녕하세요')
    print('저는 최원화입니다')

    sayhello()