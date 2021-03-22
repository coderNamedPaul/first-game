import pyautogui as pg
import random
from collections import Counter
import generator
from graph import *
root = mainWindow()
root.title('казино')
root.iconbitmap('die.ico')
windowSize(420, 180)
canvasSize(1920, 1080)

a = int(pg.prompt(text='положите деньги на счет', title='банкомат'))
def menu():
    global a
    choice = pg.confirm(text="""
    ********************************************
    приветствую тебя в нашем казино дружище!
    ********************************************
    ты можешь сыграть в: """,buttons=['рулетка', 'кости', 'однорукий бандит', 'камень ножници бумага', 'выйти'])
    if choice != 'выйти':
        pg.alert(text=a, title='твой счет')
    return choice

def rolet():
    global a
    root.title('рулетка')
    w = int(pg.prompt(text='твоя ставка'))
    c = pg.confirm(text="""
    ------------------------------------------
    РУЛЕТКА
    ------------------------------------------
    ставлю на...""", title='рулетка', buttons=['четное', 'нечетное', 'дюжина', 'свое число', 'выход'])
    e = random.randint(1, 36)
    brushColor('white')
    penColor('white')
    rectangle(0, 0, 1920, 1080)
    generator.roulet(e)
    windowSize(420, 400)
    canvasSize(1920, 1080)
    if c == 'выход':
        return
    if c == 'четное':
        a = a - w
        if e % 2 == 0:
            a = a + w * 2
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    if c == 'нечетное':
        a = a - w
        if e % 2 == 1:
            a = a + w * 2
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    if c == 'дюжина':
        a = a - w
        if e % 12 == 0:
            a = a + 6 * w
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    if c == 'свое число':
        r = int(pg.prompt(text='твое число(от 1 до 36):'))
        a = a - w
        if e == r:
            a = a + 36 * w
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    pg.alert(title='выпало', text=e)


def bones():
    global a
    windowSize(420, 400)
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    summ = first+second
    brushColor('white')
    penColor('white')
    rectangle(0, 0, 1920, 1080)
    generator.boness(first, second)

    root = mainWindow()
    root.title('сумма на костях: '+str(summ))
    windowSize(420, 180)
    canvasSize(1920, 1080)
    answ = pg.confirm(title='кости', text='выбирай', buttons=['больше', 'меньше', 'равно', 'главное меню'])
    if answ == 'больше':
        answ = 1
    elif answ == 'меньше':
        answ = 2
    elif answ == 'равно':
        answ = 3
    else:
        return
    w = int(pg.prompt(text='ставка'))
    a -= w
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    summ2 = first+second
    brushColor('white')
    penColor('white')
    rectangle(0, 0, 1920, 1080)
    generator.boness(first, second)

    root = mainWindow()
    root.title('сумма на костях: '+str(summ2))
    windowSize(420, 180)
    canvasSize(1920, 1080)
    if answ == 1:
        if summ < summ2:
            pg.alert(text='ты выиграл')
            a = a + w*2
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    elif answ == 2:
        if summ > summ2:
            pg.alert(text='ты выиграл')
            a = a + w*2
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    elif answ == 3:
        if summ == summ2:
            pg.alert(text='ты выиграл')
            a = a + w**2
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')

def oneHandBandit():
    windowSize(420, 400)
    global a
    choice = pg.confirm(title='''*********************ОДНОРУКИЙ БАНДИТ*********************''', text='''
                правила игры:
                1.совпало 2-X2
                2.совпало 3-х3
                3.совпало 4-х6
            ''', buttons=['поехали!', 'выйти'])
    if choice == 'выйти':
        return
    w = int(pg.prompt(text='ставка', title='однорукий бандит', default='100'))
    a -= w

    brushColor('white')
    penColor('white')
    rectangle(0, 0, 1920, 1080)
    slot1 = random.randint(1, 5)
    slot2 = random.randint(1, 5)
    slot3 = random.randint(1, 5)
    slot4 = random.randint(1, 5)
    generator.choice(slot1, 60)
    generator.choice(slot2, 160)
    generator.choice(slot3, 260)
    generator.choice(slot4, 360)

    root = mainWindow()
    root.title('однорукий бандит')
    windowSize(420, 180)
    canvasSize(1920, 1080)

    r=[slot1,slot2,slot3,slot4]
    t=Counter(r)
    h=[]
    for i in range(1,5):
        h.append(t[i])
    if max(h) <= 1:
        pg.alert(title='однорукий бандит', text='ты проиграл')
        pg.alert(title='твой счет', text=a)
    elif max(h) == 2:
        a = a + 2*w
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет остался прежним', text=a)
    elif max(h) == 3:
        a = a + w * 3
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет', text=a)
    elif max(h) == 4:
        a = a + w * 6
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет', text=a)
def rockPaperScissors():
    global a
    windowSize(420, 400)
    choice = pg.confirm(title="^^^^^^Камень ножници бумага^^^^^^", buttons=['камень', 'ножници', 'бумага','выход'])
    if choice == 'камень':
        choice = 1
    elif choice == 'ножници':
        choice = 2
    elif choice == 'бумага':
        choice = 3
    elif choice == 'выход':
        return
    bot = random.randint(1,3)
    w = int(pg.prompt(text='ставка'))
    a -= w
    if bot == 1:
        brushColor('white')
        penColor('white')
        rectangle(0, 0, 1920, 1080)
        image(0, 0, 'stone.jpg', anchor=NW)
        root = mainWindow()
        root.title('камень')
        windowSize(420, 180)
        canvasSize(1920, 1080)
    elif bot == 2:
        brushColor('white')
        penColor('white')
        rectangle(0, 0, 1920, 1080)
        image(0, 0, 'scissors.png', anchor=NW)
        root = mainWindow()
        root.title('ножници')
        windowSize(420, 180)
        canvasSize(1920, 1080)
    elif bot == 3:
        brushColor('white')
        penColor('white')
        rectangle(0, 0, 1920, 1080)
        image(0, 0, 'paper.jpg', anchor=NW)
        root = mainWindow()
        root.title('бумага')
        windowSize(420, 180)
        canvasSize(1920, 1080)
    if choice == 1 and bot == 1:
        pg.alert(title='камень ножници бумага', text="ничия, твой счет прежний")
        a += w
        pg.alert(title='твой счет', text=a)
    elif choice == 2 and bot == 2:
        pg.alert(title='камень ножници бумага', text="ничия, твой счет прежний")
        a += w
        pg.alert(title='твой счет', text=a)
    elif choice == 3 and bot == 3:
        pg.alert(title='камень ножници бумага', text="ничия, твой счет прежний")
        a += w
        pg.alert(title='твой счет', text=a)
    elif choice == 1 and bot == 2:
        pg.alert(title='камень ножници бумага', text="ты выиграл")
        a += w * 3
        pg.alert(title='твой счет', text=a)
    elif choice== 2 and bot == 3:
        pg.alert(title='камень ножници бумага', text="ты выиграл")
        a += w * 3
        pg.alert(title='твой счет', text=a)
    elif choice == 3 and bot == 1:
        pg.alert(title='камень ножници бумага', text="ты выиграл")
        a += w * 3
        pg.alert(title='твой счет', text=a)
    elif choice == 2 and bot == 1:
        pg.alert(title='камень ножници бумага', text="ты проиграл")
        pg.alert(title='твой счет', text=a)
    elif choice == 3 and bot == 2:
        pg.alert(title='камень ножници бумага', text="ты проиграл")
        pg.alert(title='твой счет', text=a)
    elif choice == 1 and bot == 2:
        pg.alert(title='камень ножници бумага', text="ты проиграл")
        pg.alert(title='твой счет', text=a)

while True:
    choice = menu()
    if choice == 'рулетка':
        rolet()
    elif choice == 'кости':
        bones()
    elif choice == 'однорукий бандит':
        oneHandBandit()
    elif choice == 'камень ножници бумага':
        rockPaperScissors()
    else:
        break