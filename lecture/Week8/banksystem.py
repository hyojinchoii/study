import sqlite3

db = sqlite3.connect ('C:\pytharm_prj\sample\sample.db')
class Account:

    # 멤버변수
    accno = ''
    accname = ''
    balance =''

    # 생성자

    def __int__(self, accno,accname,balance):
    #     멤버변수 초기화

        self.accno = accno
        self.accname = accname
        self.balance = balance


class Bankmanager:
    def insertAcc(Account):
        sql = "insert into Account values ('{}','{}','{}'".format(Account.accno,Account.accname,Account.balance)


    # 기본생성자 사용

    def selectAll(self):
        sql = 'select * from Account'
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()


    def main():
        while True:
            print("===Bank Menu ===")
            print("1. 계좌개설")
            print("2. 입금처리")
            print("3. 출금처리")
            print("4. 전체조회")
            print("5. 프로그램종료")
            print("==================")

            cho = input ("입력 =")

            # 계좌개설
            if cho == '1':
                accno = input ("계좌를 입력하세요.")
                accname = input ("계좌주를 입력하세요")
                balace = input( "잔고를 입력하세요")
                account = Account(accno, accname, balace)

            #     입금
            elif cho == '2':
                pass
            elif cho == '3':
                pass
            elif cho == '4':
                pass
            elif cho == '5':
                print(row)

