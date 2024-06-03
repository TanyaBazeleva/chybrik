from tkinter import *
import random as r
import time as t

# Вікно гри
vikno = Tk()
vikno.title('Flappy Bird')
vikno.geometry('1263x676')
vikno.resizable(width=False, height=False)

can = Canvas(width=1263, height=676, bg='light blue')
can.pack()

def move_up(event):
    can.itemconfig(ptashka, image=downbird)
    vvvup=can.coords(ptashka)
    kypt2=vvvup[1]-150
    can.moveto(ptashka,200,kypt2)
    def changer():
        can.itemconfig(ptashka, image=upbird)
    vikno.after(200, changer)
def standard_move():
    vvvdown=can.coords(ptashka)
    if vvvdown[1]<676:
        kypt=vvvdown[1]-10
        can.moveto(ptashka, 200, kypt)
        vikno.after(100, standard_move)
    else:
        can.moveto(ptashka,200,338)
        vikno.after(100, standard_move)

# Змінна для рахунку
score = 0

# Функція для оновлення рахунку
def update_score():
    global score
    score += 1
    score_label.config(text=f"Рахунок: {score}")

# Лейбл для відображення рахунку
score_label = Label(vikno, text=f"Рахунок: {score}", font=('Helvetica', 24), bg='light blue', fg='white')
score_label.pack()
score_label.place(x=50, y=20)

def move_stolb1():
    global stolb1
    zzz1 = can.coords(stolb1)
    if zzz1[0] > 0:
        ky1 = zzz1[0] - 42
        can.moveto(stolb1, ky1, 0)
        vikno.after(100, move_stolb1)
    else:
        can.moveto(stolb1, 1200, 0)
        can.itemconfig(stolb1, image=r.choice(listofstolbs))
        update_score()  # Оновити рахунок коли стовп переміщується назад
        vikno.after(100, move_stolb1)

def move_stolb2():
    global stolb2
    zzz2 = can.coords(stolb2)
    if zzz2[0] > 0:
        ky2 = zzz2[0] - 42
        can.moveto(stolb2, ky2, 0)
        vikno.after(100, move_stolb2)
        if zzz2[0] < 224 and zzz2[0] > 180:
            ptsh2 = can.coords(ptashka)
            hehe2 = can.itemconfig(stolb2)['image'][4]
            treba2 = loseconditions[hehe2]
            if ptsh2[1] < treba2[0] or ptsh2[1] > treba2[1]:
                vikno.destroy()
            else:
                pass
    else:
        can.moveto(stolb2, 1200, 0)
        can.itemconfig(stolb2, image=r.choice(listofstolbs))
        update_score()  # Оновлення рахунку
        vikno.after(100, move_stolb2)

def move_stolb3():
    global stolb3
    zzz3 = can.coords(stolb3)
    if zzz3[0] > 0:
        ky3 = zzz3[0] - 42
        can.moveto(stolb3, ky3, 0)
        vikno.after(100, move_stolb3)
        # Перевірка на зіткнення, коли стовп знаходиться в діапазоні потенційного контакту
        if zzz3[0] < 224 and zzz3[0] > 180:
            ptsh3 = can.coords(ptashka)
            hehe3 = can.itemconfig(stolb3)['image'][4]
            treba3 = loseconditions[hehe3]
            if ptsh3[1] < treba3[0] or ptsh3[1] > treba3[1]:
                vikno.destroy()  # Закриваємо вікно якщо сталося зіткнення
            else:
                pass
    else:
        can.moveto(stolb3, 1200, 0)
        can.itemconfig(stolb3, image=r.choice(listofstolbs))
        update_score()  # Оновлюємо рахунок коли стовп переміщується назад на початок
        vikno.after(100, move_stolb3)

def move_stolb4():
    global stolb4
    zzz4 = can.coords(stolb4)
    if zzz4[0] > 0:
        ky4 = zzz4[0] - 42
        can.moveto(stolb4, ky4, 0)
        vikno.after(100, move_stolb4)
        # Перевірка на зіткнення, коли стовп знаходиться в діапазоні потенційного контакту
        if zzz4[0] < 224 and zzz4[0] > 180:
            ptsh4 = can.coords(ptashka)
            hehe4 = can.itemconfig(stolb4)['image'][4]
            treba4 = loseconditions[hehe4]
            if ptsh4[1] < treba4[0] or ptsh4[1] > treba4[1]:
                vikno.destroy()  # Закриваємо вікно якщо сталося зіткнення
            else:
                pass
    else:
        can.moveto(stolb4, 1200, 0)
        can.itemconfig(stolb4, image=r.choice(listofstolbs))
        update_score()  # Оновлення рахунку
        vikno.after(100, move_stolb4)

def move_stolb5():
    global stolb5
    zzz5 = can.coords(stolb5)
    if zzz5[0] > 0:
        ky5 = zzz5[0] - 42
        can.moveto(stolb5, ky5, 0)
        vikno.after(100, move_stolb5)
        # Перевірка на зіткнення, коли стовп знаходиться в діапазоні потенційного контакту
        if zzz5[0] < 224 and zzz5[0] > 180:
            ptsh5 = can.coords(ptashka)
            hehe5 = can.itemconfig(stolb5)['image'][4]
            treba5 = loseconditions[hehe5]
            if ptsh5[1] < treba5[0] or ptsh5[1] > treba5[1]:
                vikno.destroy()  # Закриваємо вікно, якщо сталося зіткнення
            else:
                pass
    else:
        can.moveto(stolb5, 1200, 0)
        can.itemconfig(stolb5, image=r.choice(listofstolbs))
        update_score()  # Оновлення рахунку
        vikno.after(100, move_stolb5)

first=PhotoImage(file='stolb1.png')
second=PhotoImage(file='stolb2.png')
third=PhotoImage(file='stolb3.png')
fourth=PhotoImage(file='stolb4.png')
fifth=PhotoImage(file='stolb5.png')
sixth=PhotoImage(file='stolb6.png')
upbird=PhotoImage(file='upbird.png')
downbird=PhotoImage(file='downbird.png')
    #Sorting files with pillar to list
listofstolbs=[first, second, third, fourth, fifth, sixth]
loseconditions={'pyimage1':[175,330],'pyimage2':[415,570],'pyimage3':[230,390],'pyimage4':[255,415],'pyimage5':[175,310],'pyimage6':[410,570]}
    #Creating objects
stolb1=can.create_image(1200, 338, image=r.choice(listofstolbs))
stolb2=can.create_image(1200, 338, image=r.choice(listofstolbs))
stolb3=can.create_image(1200, 338, image=r.choice(listofstolbs))
stolb4=can.create_image(1200, 338, image=r.choice(listofstolbs))
stolb5=can.create_image(1200, 338, image=r.choice(listofstolbs))
ptashka=can.create_image(200, 338, image=upbird)
    #Binds
can.bind_all('w', move_up)
    #Standard actions
vikno.after(100, standard_move)
vikno.after(1000,move_stolb1)
vikno.after(4000,move_stolb2)
vikno.after(7000,move_stolb3)
vikno.after(10000,move_stolb4)
vikno.after(13000,move_stolb5)

vikno.mainloop()