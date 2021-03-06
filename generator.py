from graph import *
from random import randint
# первый икс равен 60 каждий следующий +100 y всегда 50


def triangle(x, y):
    penSize(3)
    brushColor('green')
    penColor('green')
    polygon([(x, y), (x+40, y+60), (x-40, y+60), (x, y)])


def romb(x, y):
    penSize(3)
    brushColor(255, 204, 0)
    penColor(255, 204, 0)
    polygon([(x, y - 30), (x+40, y+30), (x, y + 90), (x-40, y+30), (x, y - 30)])


def square(x, y):
    penSize(3)
    brushColor(0, 148, 214)
    penColor(0, 148, 214)
    rectangle(x - 30, y, x + 30, y + 60)


def notSquare(x, y):
    penSize(3)
    brushColor(247, 109, 0)
    penColor(247, 109, 0)
    rectangle(x - 40, y - 30, x + 40, y + 90)


def circle2(x, y):
    penSize(3)
    brushColor(241, 54, 60)
    penColor(241, 54, 60)
    circle(x, y+30, 40)


def choice(figure, x):
    y = 50
    if figure == 1:
        triangle(x, y)
    elif figure == 2:
        romb(x, y)
    elif figure == 3:
        square(x, y)
    elif figure == 4:
        notSquare(x, y)
    elif figure == 5:
        circle2(x, y)

def boness(value1, value2):
    penColor('black')
    penSize(6)
    rectangle(80, 20, 200, 140)
    rectangle(220, 20, 340, 140)
    penSize(1)
    brushColor('black')
    if value1 == 1:
        circle(140, 80, 10)
    elif value1 == 2:
        circle(140, 105, 10)
        circle(140, 55, 10)
    elif value1 == 3:
        circle(140, 115, 10)
        circle(140, 80, 10)
        circle(140, 45, 10)
    elif value1 == 4:
        circle(110, 105, 10)
        circle(170, 105, 10)
        circle(110, 55, 10)
        circle(170, 55, 10)
    elif value1 == 5:
        circle(110, 105, 10)
        circle(170, 105, 10)
        circle(140, 80, 10)
        circle(110, 55, 10)
        circle(170, 55, 10)
    elif value1 == 6:
        circle(170, 115, 10)
        circle(170, 80, 10)
        circle(170, 45, 10)
        circle(110, 115, 10)
        circle(110, 80, 10)
        circle(110, 45, 10)
    if value2 == 1:
        circle(280, 80, 10)
    elif value2 == 2:
        circle(280, 105, 10)
        circle(280, 55, 10)
    elif value2 == 3:
        circle(280, 115, 10)
        circle(280, 80, 10)
        circle(280, 45, 10)
    elif value2 == 4:
        circle(250, 105, 10)
        circle(310, 105, 10)
        circle(250, 55, 10)
        circle(310, 55, 10)
    elif value2 == 5:
        circle(250, 105, 10)
        circle(310, 105, 10)
        circle(280, 80, 10)
        circle(250, 55, 10)
        circle(310, 55, 10)
    elif value2 == 6:
        circle(310, 115, 10)
        circle(310, 80, 10)
        circle(310, 45, 10)
        circle(250, 115, 10)
        circle(250, 80, 10)
        circle(250, 45, 10)

def roulet(value):
    x =185
    y =65
    brushColor('yellow')
    penColor('yellow')
    polygon([(210, 125), (180, 175), (240, 175), (210, 125)])
    if value % 2 == 0 and value % 12 != 0:
        brushColor('red')
        penColor('red')
        rectangle(x, y, x+50, y+50)
        rectangle(x-120, y, x-70, y+50)
        rectangle(x+120, y, x+170, y+50)
        penColor('black')
        brushColor('black')
        rectangle(x-180, y, x-130, y+50)
        rectangle(x-60, y, x-10, y+50)
        rectangle(x+60, y, x+110, y+50)
        rectangle(x+180, y, x+230, y+50)
        penColor('green')
        brushColor('green')
        kolhos = randint(1, 5)
        if kolhos == 1:
            rectangle(x - 120, y, x - 70, y + 50)
        elif kolhos == 2:
            rectangle(x + 120, y, x + 170, y + 50)
        else:
            pass
    elif value % 2 == 1:
        penColor('black')
        brushColor('black')
        rectangle(x, y, x + 50, y + 50)
        rectangle(x - 120, y, x - 70, y + 50)
        rectangle(x + 120, y, x + 170, y + 50)

        brushColor('red')
        penColor('red')
        rectangle(x - 180, y, x - 130, y + 50)
        rectangle(x - 60, y, x - 10, y + 50)
        rectangle(x + 60, y, x + 110, y + 50)
        rectangle(x + 180, y, x + 230, y + 50)

        penColor('green')
        brushColor('green')
        kolhos = randint(1, 6)
        if kolhos == 1:
            rectangle(x - 180, y, x - 130, y + 50)
        elif kolhos == 2:
            rectangle(x - 60, y, x - 10, y + 50)
        elif kolhos == 3:
            rectangle(x + 60, y, x + 110, y + 50)
        elif kolhos == 4:
            rectangle(x + 180, y, x + 230, y + 50)
        else:
            pass
    elif value % 12 == 0:
        brushColor('red')
        penColor('red')
        rectangle(x - 120, y, x - 70, y + 50)
        rectangle(x + 120, y, x + 170, y + 50)
        penColor('black')
        brushColor('black')
        rectangle(x - 180, y, x - 130, y + 50)
        rectangle(x - 60, y, x - 10, y + 50)
        rectangle(x + 60, y, x + 110, y + 50)
        rectangle(x + 180, y, x + 230, y + 50)
        brushColor('green')
        penColor('green')
        rectangle(x, y, x + 50, y + 50)
