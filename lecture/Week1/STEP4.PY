money = 2500

if money >= 3000:
    print("택시 타자")
else:
    print("걸어 가자")

    # 입력 숫자의 홀수 짝수 구분하기
    num1 = int(input("숫자를 입력하세요"))

    if num1 % 2 > 0 :
        print("홀수")
    else:
        print("짝수")


# import(datetime)
today = datetime.datetime.now()
print(today)

day = today.weekday()
print(day)

# 0~4 평일, 5~6 주말

day = int(input("숫자를 입력하세요"))

if day>= 5:
    print("주말")
else:
    print("평일")

# 다중 if문
# 출력형식 => 점수: 85 등급: B

Grand = int(input("score를 입력하세요"))

if score >= 90:
    grade = "A"
elif:score>=80:
    grand = "B"
elif:score >=70:
    grand = "C"
else:score >60:
grand= "D"

print(grand)

if score>= 60:
grade = "합격"
else:
grade="불합격"

# 삼항연산자
grade = "합격" if score >= 60 else "불합격"
print(grade)


eng = 70; math= 50

if eng = 80 and math = 80:
print("합격")
else:
print("불합격")

# 연습문제
day = int(input("숫자를 입력하세요"))

if day>= 5:
    print("주말")
else:
    print("평일")

today = datetime.datetime.noww()
month = today.month
if daytime=3 and 4 and 5:
print("현재는 봄입니다.")

elif daytime=6 and 7 and 8:
print("현재는 여름입니다.")

elif daytime = 9 and 10 and 11:
print( "현재는 가을입니다.")

else: print( "현재는 겨울입니다.")


# 중첩 if 문

sex="남"
age= 13

#남자이면서, 초등학생 (8-13), 중학생 (14~16), 고등학생 (17~19) 유아(~8) 나머지 성인

if sex == "남":
if age < 8 :
print ("남자 유아입니다")
else :
if age < 8 :
print ("여자 유아입니다")

if sex == "남":
if 8 =< age =< 13:
print("남자 초등학생입니다")
else :
if 8 =< age =< 13:
print("여자 초등학생입니다.")

#>