# -- coding: utf-8 --

from tkinter import *
from tkinter import messagebox

def d1():
    arg = txt.get()
    i = 1
    N = int(txt.get())
    result = ""
    while i**2 <= N:
        result += str(i**2) + ' '
        i += 1
    messagebox.showinfo('Результат', result)

def d2():
    arg = txt1.get()
    i = 2
    N = int(txt1.get())
    if N >= 2:
     while N % i != 0:
        i += 1
     messagebox.showinfo('Результат', i)
    else:
     messagebox.showinfo('Результат', 'No')

def d3():
    arg = txt2.get()
    N = int(txt2.get())
    i = 0
    a = 1
    while a*2 <= N:
        a *= 2
        i += 1
    messagebox.showinfo('Результат', "Показатель степени: " + str(i) + " " + "степень: " + str(a))

def d4():
    x = int(txt3_1.get())
    y = int(txt3_2.get())
    n = 1
    while x < y:
        x += x * 0.1
        n += 1
    messagebox.showinfo('Результат', n)

l1 = 0
def d5():
    global l1
    arg = int(txt4.get())
    if arg != 0:
        l1 += 1
    else:
        messagebox.showinfo('Результат', l1)
        l1 = 0
    txt4.delete(0, END)

l2 = 0
S = 0
def d6():
    global l2
    global S
    arg = int(txt5.get())
    if arg != 0:
        l2 +=1
        S += arg
    else:
        messagebox.showinfo('Результат', S / l2)
        l2 = 0
        S = 0
    txt5.delete(0, END)

m = 0
S = 0
def d7():
    global m
    global S
    n = int(txt6.get())
    if m > 0:
     if n > m:
         S += 1
    m = n
    
    if(n == 0):
        messagebox.showinfo('Результат', S)
        m = 0
        S = 0
    txt6.delete(0, END)

m1 = 0
S1 = 1
M = 0
def d8():
    global m1
    global S1
    global M
    n = int(txt7.get())
    if m1 > 0:
      if n == m1:
       S1 += 1
      else:
        S1 = 1
      if S1 > M:
        M = S1
    m1 = n

    if n == 0:
        messagebox.showinfo('Результат', M)
        m1 = 0
        S1 = 1
        M = 0
    txt7.delete(0, END)

window = Tk()
window.title("N6")
window.geometry('700x300')
lbl = Label(window, text = "Введите целое число")
lbl.grid(column=0, row = 0)
txt = Entry(window, width = 10)
txt.grid(column=1, row = 0)
btn = Button(window, text = "N5_1", command = d1)
btn.grid(column=2, row = 0)

lbl1 = Label(window, text = "Введите число не меньше 2")
lbl1.grid(column=0, row = 1)
txt1 = Entry(window, width = 10)
txt1.grid(column=1, row = 1)
btn1 = Button(window, text = "N5_2",command = d2)
btn1.grid(column=2, row = 1)

lbl2 = Label(window, text = "Введите натуральное число")
lbl2.grid(column=0, row = 2)
txt2 = Entry(window, width = 10)
txt2.grid(column=1, row = 2)
btn2 = Button(window, text = "N5_3", command = d3)
btn2.grid(column=2, row = 2)

lbl3 = Label(window, text = "Введите 2 действительных числа")
lbl3.grid(column=0, row = 3)
txt3_1 = Entry(window, width = 10)
txt3_1.grid(column=1, row = 3)
txt3_2 = Entry(window, width = 10)
txt3_2.grid(column=2, row = 3)
btn3 = Button(window, text = "N5_4", command = d4)
btn3.grid(column=3, row = 3)

lbl4_1 = Label(window, text = "Введите числа по одному. Чтобы завершить, введите 0")
lbl4_1.grid(column=0, row = 4)
txt4 = Entry(window, width = 10)
txt4.grid(column=1, row = 4)
btn4 = Button(window, text = "N5_5", command = d5)
btn4.grid(column=2, row = 4)

lbl5 = Label(window, text = "Введите числа по одному. Чтобы завершить, введите 0")
lbl5.grid(column=0, row = 5)
txt5 = Entry(window, width = 10)
txt5.grid(column=1, row = 5)
btn5 = Button(window, text = "N5_6", command = d6)
btn5.grid(column=2, row = 5)

lbl6 = Label(window, text = "Введите числа по одному. Чтобы завершить, введите 0")
lbl6.grid(column=0, row = 6)
txt6 = Entry(window, width = 10)
txt6.grid(column=1, row = 6)
btn6 = Button(window, text = "N5_7", command = d7)
btn6.grid(column=2, row = 6)

lbl7 = Label(window, text = "Введите числа по одному. Чтобы завершить, введите 0")
lbl7.grid(column=0, row = 7)
txt7 = Entry(window, width = 10)
txt7.grid(column=1, row = 7)
btn7 = Button(window, text = "N5_8", command = d8)
btn7.grid(column=2, row = 7)

window.mainloop()