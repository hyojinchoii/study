import sqlite3

print(sqlite3.sqlite_version_info)

try :
    # 데이터베이스 연결
    con = sqlite3.connect('C:\pytharm_prj\sample\sample.db')
    cursor = con.cursor()

    def getlist():
        sql = 'select * from student'
        cursor.execute(sql)
        data = cursor.fetchall()

        print(type(data))
        print(data)

        for row in data:
            print(row)

    def select(name):
        sql = "select * from student where name = '{}'".format(name)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)

    print('======목록확인=======')
    getlist()
    print('======한개 데이터 확인=======')
    select('강호동')

#     업데이트
#     insert, update, delete  ----> commit이 필요함

    # def update(name):
    #     sql = "update student set major '디자인' where name ='{}'".format(name)
    #     cursor.execute(sql)
    #     con.commit()
    # update('최호동')
    # print('======업데이트 확인=======')
    # getlist()

# 딜리트

    def delete(name):
        sql = "delete from student where name = '{}'".format(name)
        cursor.execute(sql)
        con.commit()
    delete('강호동')
    print('======삭제 확인=======')
    getlist()

# 인설트
    def insert():
        sql = "insert into student value (8,'김미미', '경영학과',50,20,80)"
        cursor.execute(sql)
        con.commit()
    print('======입력 확인=======')
    getlist()



except Exception as e :
    print(e)

finally:
    pass
