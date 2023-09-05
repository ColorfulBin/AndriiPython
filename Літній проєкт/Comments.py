"""
Программа "Графіки" - це програма, у якій завдяки кнопкам, створені інструментами
із бібліотеки tkinter, виводяться графіки, створені інструментами із бібліотеки
turtle. Також, у программі використана бібліотека math для виконування складних
обчислень, такі як косінус на сінус.

Метод роботи программи:
Спочатку, ми створюємо самі графіки окремими функціями(приклади: logSpiral, pascRavlik).
Далі, ми створюємо вікно з 13 кнопками, де з'єднуємо кнопки з відповідними їм
графіками. При нажаті на кнопку викликається відповідна їй функція, яка запускає
меню turtle з графіком. Зауважимо, що перед викликом деяких функцій, здійснюється
запит у терміналі.
"""

"""
Імпортуємо бібліотеки turtle, math, tkinter.
"""
import turtle
import math
import tkinter

"""
Створюємо графік логарифмічної спіралі. Лінії 27-33 відповідають за декоративну
складову меню, лінії 34-51 створюють сітку, лінії 52-62 відповідають за сам
графік.
"""
def logSpiral():
    turtle.title("Логарифмічна спіраль")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(1, 52):
        a=10*3.14*(i-1)/100
        exp=2.71**(0.2*a)
        r=5*exp
        x=r*math.cos(a)
        y=r*math.sin(a)
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік Архімедової спіралі. Лінії 70-75 відповідають за декоративну
складову меню, лінії 76-93 створюють сітку, лінії 94-102 відповідають за сам
графік.
"""
def archSpiral():
    turtle.title("Архімедова спіраль")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(1, 252):
        a=10*3.14*(i-1)/100
        x=a*math.cos(0.5*a)
        y=a*math.sin(0.5*a)
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік равлика Паскаля. Лінії 109-115 відповідають за декоративну
складову меню, лінії 116-133 створюють сітку, лінії 134-143 відповідають за сам
графік.
"""
def pascRavlkik():
    turtle.title("Равлик Паскаля")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(1, 42):
        a=2*3.14*(i-1)/40
        r=80-150*math.cos(a)
        x=r*math.cos(a)
        y=r*math.sin(a)
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік ліній Хреста. Лінії 150-156 відповідають за декоративну
складову меню, лінії 157-174 створюють сітку, лінії 175-188 відповідають за сам
графік.
"""
def linChrest():
    turtle.title("Лінія 'Хрест'")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(1, 202):
        a=2*3.14*(i-1)/200
        c=math.sin(2*a)
        if c!=0:
            r=50/c
            x=r*math.cos(a)
            y=r*math.sin(a)
            if y == -817.0229336721669 or x == -838.8436203249894 or y == 861.8624062913411:
                turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік локон Анієзи. Лінії 195-201 відповідають за декоративну
складову меню, лінії 202-219 створюють сітку, лінії 220-228 відповідають за сам
графік.
"""
def locAniezy():
    turtle.title("Локон Анієзи")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-50, 52):
        a=5*i
        x=a
        y=240000/(a**2 + 5000)
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік конхоїди Ніхомеда. Лінії 235-241 відповідають за декоративну
складову меню, лінії 242-259 створюють сітку, лінії 260-281 відповідають за сам
графік.
"""
def conNihomeda():
    turtle.title("Конхоїда Ніхомеда")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-100, 102):
        a=2*i
        if (a-10)**2!= 0:
            d=3600*a**2/(a-10)**2 - a**2
            if d>=0:
                x=a
                y=d**0.5
                turtle.goto(x,y)
                turtle.pendown()
    turtle.penup()
    for i in range(-100, 102):
        a=2*i
        if (a-10)**2 != 0:
            d=3600*a**2/(a-10)**2 - a**2
            if d>=0:
                x=a
                y=-d**0.5
                turtle.goto(x,y)
                turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік лінії Ланцюга. Лінії 288-294 відповідають за декоративну
складову меню, лінії 295-312 створюють сітку, лінії 313-321 відповідають за сам
графік.
"""
def linLantsuga():
    turtle.title("Лінія ланцюга")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-100, 102):
        a=5*i
        x=a
        y=-30*(math.exp(a/30)-math.exp(-a/30))/2
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік астродїди. Лінії 328-334 відповідають за декоративну
складову меню, лінії 335-352 створюють сітку, лінії 353-361 відповідають за сам
графік.
"""
def astroida():
    turtle.title("Астроїда")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(1, 202):
        a=20*3.14*i
        x=70*math.cos(a)**3
        y=-70*math.sin(a)**3
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік лінії Декарта. Лінії 368-374 відповідають за декоративну
складову меню, лінії 375-392 створюють сітку, лінії 393-403 відповідають за сам
графік.
"""
def lysDecarta():
    turtle.title("Листок Декарта")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-200, 202):
        a=i/10
        d=a**3+1
        if d!=0:
            x=90*a/d
            y=-90*a**2/d
            turtle.goto(x,y)
            turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік циклоїди. Лінії 410-416 відповідають за декоративну
складову меню, лінії 417-434 створюють сітку, лінії 435-443 відповідають за сам
графік.
"""
def tsycloida():
    turtle.title("Циклоїда")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-100, 102):
        a=3.14*i/10
        x=15*a+20*math.sin(a)
        y=-15+20*math.cos(a)
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо лінійний графік. Лінії 450-458 відповідають за декоративну
складову меню, а також отримують змінні для графіку, лінії 459-476 
створюють сітку, лінії 477-484 відповідають за сам графік.
"""
def linGraphic():
    turtle.title("Лінійний графік: y=ax+b")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    a=float(input("a?"))
    b=float(input("b?"))
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-10, 11):
        x=(i-b)/a*50
        y=i*50
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік параболи. Лінії 491-499 відповідають за декоративну
складову меню, а також отримують змінні для графіку, лінії 500-517
створюють сітку, лінії 518-525 відповідають за сам графік.
"""
def parabola():
    turtle.title("Парабола: y=ax*х+b")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    a=float(input("a?"))
    b=float(input("b?"))
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-50, 51):
        x=i*12.5
        y=(i*i*a+4*b)*12.5
        turtle.goto(x,y)
        turtle.pendown()
    turtle.exitonclick()

"""
Створюємо графік гіперболи. Лінії 532-540 відповідають за декоративну
складову меню, а також отримують змінні для графіку, лінії 541-558
створюють сітку, лінії 559-569 відповідають за сам графік.
"""
def hiberbola():
    turtle.title("Гіпербола: y=a/x+b")
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.speed(0)
    a=float(input("a?"))
    b=float(input("b?"))
    turtle.bgcolor("white")
    turtle.color("black")
    for i in range(1,10):
        turtle.penup()
        turtle.goto(i*50-250,-250)
        turtle.pendown()
        turtle.goto(i*50-250,250)
        turtle.penup()
        turtle.goto(-250, i * 50 - 250)
        turtle.pendown()
        turtle.goto(250, i * 50 - 250)
    turtle.width(3)
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.color("green")
    turtle.penup()
    for i in range(-250, 251):
        if i != 0:
            x=i
            y=(a*10/i)*250+b*50
            if i == 1:
                turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
    turtle.exitonclick()

"""
Створюємо меню і редагуємо його розмір і підпис
"""
window = tkinter.Tk()
window.title("Графіки")
window.geometry("500x700")
"""
Створюємо кнопки, підписуємо, з'єднуємо з функціями графіків
"""
button1 = tkinter.Button(window, text="Логарифмічна спіраль", background="gray", command=logSpiral)
button2 = tkinter.Button(window, text="Архімедова спіраль", background="gray", command=archSpiral)
button3 = tkinter.Button(window, text="Равлик Паскаля", background="gray", command=pascRavlkik)
button4 = tkinter.Button(window, text="Лінія 'Хрест'", background="gray", command=linChrest)
button5 = tkinter.Button(window, text="Локон Анієзи", background="gray", command=locAniezy)
button6 = tkinter.Button(window, text="Конхаїда Ніхомеда", background="gray", command=conNihomeda)
button7 = tkinter.Button(window, text="Лінія ланцюга", background="gray", command=linLantsuga)
button8 = tkinter.Button(window, text="Астроїда", background="gray", command=astroida)
button9 = tkinter.Button(window, text="Листок Декарта", background="gray", command=lysDecarta)
button10 = tkinter.Button(window, text="Циклоїда", background="gray", command=tsycloida)
button11 = tkinter.Button(window, text="Лінійний графік з вводом чисел", background="gray", command=linGraphic)
button12 = tkinter.Button(window, text="Парабола з вводом чисел", background="gray", command=parabola)
button13 = tkinter.Button(window, text="Гіпербола з вводом чисел", background="gray", command=hiberbola)
"""
Підпис учня на роботі
"""
button14 = tkinter.Label(text="Виконано учнем 21-М групи\n Андрієм Дирдою")
"""
Додаємо кнопки на меню
"""
button1.place(height=100, width=250, x=0, y=0)
button2.place(height=100, width=250, x=0, y=100)
button3.place(height=100, width=250, x=0, y=200)
button4.place(height=100, width=250, x=0, y=300)
button5.place(height=100, width=250, x=0, y=400)
button6.place(height=100, width=250, x=250, y=0)
button7.place(height=100, width=250, x=250, y=100)
button8.place(height=100, width=250, x=250, y=200)
button9.place(height=100, width=250, x=250, y=300)
button10.place(height=100, width=250, x=250, y=400)
button11.place(height=100, width=250, x=0, y=500)
button12.place(height=100, width=250, x=0, y=600)
button13.place(height=100, width=250, x=250, y=500)
button14.place(height=100, width=250, x=250, y=600)
"""
Запускаємо меню
"""
window.mainloop()