from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('300x360')

price = {'로제떡볶이': 16000, '치킨':30000, '커피':10000, '까르보나라':20000, '보쌈':150000, '와플':3000}

def order(item):
    order_list.insert(INSERT, item+'\n')
    item_price = price.get(item)
    global total
    total += item_price
    total_label['text'] = '금액:' + str(total) + '원'


bframe = Frame(window)

b1 =Button(bframe,text='로제떡볶이',width=10, command= lambda:order('로제떡볶이'))
b2 =Button(bframe,text='치킨',width=10,command= lambda:order('치킨'))
b3 =Button(bframe,text='커피',width=10,command= lambda:order('커피'))
b4 =Button(bframe,text='까르보나라',width=10,command= lambda:order('까르보나라'))
b5 =Button(bframe,text='보쌈',width=10,command= lambda:order('보쌈'))
b6 =Button(bframe,text='와플',width=10,command= lambda:order('와플'))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

bframe.pack(side = 'top')

total_label = Label(window,text = '합계:0월',width=10, height =2, fg = 'blue')
total_label.pack()

bframe.pack(side = 'top')
window.mainloop()

order_list = Text(window)
order_list.pack()