from tkinter import *
from tkinter import messagebox

def msg():
    messagebox.showinfo('카카오프렌즈','프렌즈 귀엽죠?')

def msg2():
    messagebox.showinfo('구독', '좋아요')

window = Tk()
window.geometry('400x600')

photo = PhotoImage(file = '../week6/meta-data/images/101.png')
button1 = Button(window, image = photo,command=msg)
button2 = Button(window,text = '좋아요',command=msg2)
button3 = Button(window,text = '좋아요',command=quit)

bframe = Frame(window)
b1 = Button(bframe, text = 'North')
b2 = Button(bframe, text = 'East')
b3 = Button(bframe, text = 'West')
b4 = Button(bframe, text = 'South')

# 상대좌표 배치
button1.pack()

# 절대좌표 배치
button2.place(x=140, y=450)
button3.pack(x=190, y=450)

# grid 배치

b1.grid(row=0, column=0)
b3.grid(row=1, column=0)
b2.grid(row=1, column=1)
b4.grid(row=2, column=0)


bframe.pack(side= 'bottom')



# 상대좌표 배치
button1.pack()

# 절대좌표 배치
button2.place(x=140, y=450)
button3.pack(x=190, y=450)
window.mainloop()

button1.pack()
window.mainloop()

