import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x300')
window.title = 'zhopa s ushami'


def calculate_bmi():
    kg = int(low_tf.get())
    m = int(heigh_tf.get())
    m /= 100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

heigh_lb = Label(
    frame,
    text='Введите свой рост (в см)'
)
heigh_lb.grid(row=3, column=1)

low_lb = Label(
    frame,
    text='Введите свой вес (в кг)'
)
low_lb.grid(row=4, column=1)

heigh_tf = Entry(
    frame
)
heigh_tf.grid(row=3, column=2)

low_tf = Entry(
    frame
)
low_tf.grid(row=4, column=2)

cal_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calculate_bmi
)
cal_btn.grid(row=5, column=2)


window.mainloop()
