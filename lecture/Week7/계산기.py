from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('240x360')

def click(value):
    # messagebox.showinfo('',value)

    if '=' in show_txt.get():
        show_txt.delete(0,END)

    if value == '=' :
        calc()
    else:
        show_txt.insert(END,value)


def calc():
    cal_txt = show_txt.get()
    # messagebox.showinfo('',cal_txt)
    show_txt.insert(END, '='+str(eval(show_txt.get())))

def clear():
    show_txt.delete(0,END)



# 입력창, 계산버튼

top_frame = Frame(window)
show_txt = Entry(top_frame,width=20)
e_btn = Button(top_frame,text='삭제',width=10,command = clear)
show_txt.grid(row=0, column=0)
e_btn.grid(row=0, column=1)

frame_bot = Frame(window)
b_min = Button(frame_bot, text = '-',width=10, command=lambda:click('-'))
b_plus = Button(frame_bot, text = '+',width=10, command=lambda:click('+'))
b0 = Button(frame_bot, text = '0',width=10, command=lambda:click('0'))
b1 = Button(frame_bot, text = '1',width=10, command=lambda:click('1'))
b2 = Button(frame_bot, text = '2',width=10, command=lambda:click('2'))
b3 = Button(frame_bot, text = '3',width=10, command=lambda:click('3'))
b4 = Button(frame_bot, text = '4',width=10, command=lambda:click('4'))
b5 = Button(frame_bot, text = '5',width=10, command=lambda:click('5'))
b6 = Button(frame_bot, text = '6',width=10, command=lambda:click('6'))
b7 = Button(frame_bot, text = '7',width=10, command=lambda:click('7'))
b8 = Button(frame_bot, text = '8',width=10, command=lambda:click('8'))
b9 = Button(frame_bot, text = '9',width=10, command=lambda:click('9'))


# grid 배치

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=0, column=0)
b8.grid(row=0, column=1)
b9.grid(row=0, column=2)

b0.grid(row=3, column=1)
b_min.grid(row=3, column=0)
b_plus.grid(row=3, column=2)

top_frame.pack()
frame_bot.pack()
frame_bot.pack(side='top')
frame_bot.pack(side='bottom')

window.mainloop()
