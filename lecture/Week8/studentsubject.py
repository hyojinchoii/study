
import sqlite3

# 데이터베이스 연결 전역변수
con = sqlite3.connect('C:\pytharm_prj\sample\sample.db')

def insert():
    name = input('이름입력: ')

    # 기존학생 데이터 존재 여부 확인
    cur = con.cursor()
    sql = "select name from student where name = '{}'".format(name)
    data = cur.execute(sql)
    # print(type(data), str(len(data)))
    if name in data:
        print("학생이 존재합니다")
    else:

   # 성적 입력
            major = input('전공을 입력하세요: ')
            sub1 = int(input('과목 1 성적을 입력하세요: '))
            sub2 = int(input('과목 2 성적을 입력하세요: '))
            sub3 = int(input('과목 3 성적을 입력하세요: '))
            total = sub1+sub2+sub3
            average = round(total/3,3)

            try:
                cur = con.cursor()
                # sql = "insert into student(name, major, sub1, sub2, sub3,total,average) values ('{}','{}',{},{},{},{},{})".format(name,major,sub1,sub2,sub3,total,average)
                # cur.execute(sql)

                sql = "insert into student(name, major, sub1, sub2, sub3,total,average) values(?,?,?,?,?,?,?) "
                cur.execute(sql,(name,major,sub1,sub2,sub3,total,average))
                con.commit()
                print('성적이 입력되었습니다.')

            except Exception as e:
                print(e)
                con.rollback()
                con.close()

def selectall():
    try:
        cur = con.cursor()
        sql = "select * from student"
        data = cur.execute(sql)


        for s in data:
            print(s)
    except Exception as e:
        print(e)
        con.rollback()


def selectName():
    try:
        name = str(input("이름을 입력하세요: "))
        cur = con.cursor()
        sql = "SELECT * FROM student where name = '{}'".format(name)
        data = cur.execute(sql)


        for s in data:
            print(s)

    except Exception as e:
        print(e)
        con.rollback()

def selectrename():
    try:
        name = str(input("수정할 이름을 입력하세요: "))
        sub1 = int(input('과목 1 성적을 입력하세요: '))
        sub2 = int(input('과목 2 성적을 입력하세요: '))
        sub3 = int(input('과목 3 성적을 입력하세요: '))
        cur = con.cursor()
        sql = "update  student set sub1 ={},sub2 = {}, sub3 ={} where name = '{}'".format(sub1,sub2,sub3,name)
        data = cur.execute(sql)
        con.commit()
        print(sql)

        for s in data:
            print(s)

    except Exception as e:
        print(e)
        con.rollback()


def selectdelete():
    try:
        name = str(input("삭제할 이름을 입력하세요: "))
        cur = con.cursor()
        sql = "delete from student WHERE name = '{}'".format(name)
        data = cur.execute(sql)
        con.commit()

        for s in data:
            print(s)

    except Exception as e:
        print(e)
        con.rollback()



def main():
    print()
    print()
    print("-------------------------------------성적입력-----------------------------------")
    print()
    print()
    print()
    print()
    print()
    print("---------------------------------------------------------------------------------")

    while True:
        select = input("1. 입력 2. 출력 3. 검색 4. 수정 5.삭제 6.종료 \n")


        # 성적입력
        if select == '1':
            # 입력 함수 호출
            insert()


        # 성적출력
        elif select == '2':

            selectall()


        # 학생검색
        elif select == '3':

            selectName()


        # 학생수정
        elif select== '4':

           selectrename()


        # 학생 삭제
        elif select == '5':
            selectdelete()


        elif select == '6':
            break

main()