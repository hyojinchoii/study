import tkinter
from tkinter import *
import tkinter.font as tkFont
import sqlite3
from tkinter import messagebox


def insertName():
    try:
        con = sqlite3.connect('C:\pytharm_prj\sample\sample.db')
        cursor = con.cursor()
        sql= "insert into ranking(username,point) VALUES ('{}',{})".format(str(myname.get(),str(mypoint.get())))
        cursor.execute(sql)
        con.commit()
        print('이름 입력됨')
    except Exception as e:
        print(e)
    finally:
        pass

#  ==========================화면 띄우기
window = Tk()
window.geometry('440x360')


# 한글폰트지정
fontstyle= tkFont.Font(family="굴림", size=15)
title = Label(window, text = "10초동안 버튼 누르기", anchor= "center", font = fontstyle)
title.pack()

name = Label (window, text = "이름:")
name.place(x=90, y=50)

myname = StringVar()
name_txt = tkinter.Entry(window,textvariable = myname,width=20)
name_txt.place(x=130, y=50)

mypoint = StringVar()
point_txt = tkinter.Entry(window,textvariable=mypoint,width=5)
point_txt.place(x=160, y=50)

name_btn = Button(window, text = "이름입력", width=20, height=2, command=insertName)
name_btn.place(x=120, y=90)


window.mainloop()

