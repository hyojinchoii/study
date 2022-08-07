#문제 1
#
weight = int(input("짐의 무게는 얼마입니까?"))

if weight < 10 :
    print("수수료는 없습니다")
else :
    print("수수료는 10,000원 입니다.")

# 문제 2

weight = int(input("짐의 무게는 얼마입니까?"))

if weight < 10 :
    print("수수료는 없습니다")

elif weight > 10 :
    print("수수료는 {0}입니다.".format(weight/10*10000))

# 문제 3

    while True:
        num = int(input("예상 숫자를 입력하시오 :"))
        com= random.randint(1,10)

        if num == com :
            print("~~성공~~")
            break
        elif num < com:
            print("더 작은 수 입력")
            continue
        else:
            print("더 큰 수 입력")
            continue

# 연습문제 3

for i in range(1,101):
    if i % 2 != 0 and i % 3 ==0 :
        print(i)

