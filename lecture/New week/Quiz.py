
balance = 0

# 잔액확인

def getbalance ():
    print('잔액확인:', format(balance,"3,d"))

# 입금

def deposit (money):
    global balance
    balance += money

    print(format(money, "3,d")+"원이 입금되었습니다")


# 출금
def withdraw (money):
    global balance
    balance -= money

    if balance > money :
        print(format(money, "3,d") + "원이 출금되었습니다.")
        print(format(balance, "3,d") + "원이 남았습니다.")
    else:
        print("잔액이 부족합니다.")

deposit (100000)
withdraw (12000)
withdraw(5000)
deposit(500000)
withdraw(30000)

getbalance()
