import pyautogui as pg
import random
from collections import Counter
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
    c = pg.confirm(text="""
    ------------------------------------------
    РУЛЕТКА
    ------------------------------------------
    ставлю на...""", title='рулетка', buttons=['четное', 'нечетное', 'дюжина', 'свое число', 'выход'])
    if c == 'выход':
        return
    if c == 'четное':
        w = int(pg.prompt(text='твоя ставка'))
        e = random.randint(1, 36)
        if e % 2 == 0:
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            a = a - w
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    if c == 'нечетное':
        w = int(pg.prompt(text='твоя ставка'))
        e = random.randint(1, 36)
        if e % 2 == 1:
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            a = a - w
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    if c == 'дюжина':
        w = int(pg.prompt(text='твоя ставка'))
        a = a - w
        e = random.randint(1, 36)
        if e % 12 == 0:
            a = a + 3 * w
            pg.alert(text='ты выиграл')
            pg.alert(text=a, title='твой счет')
        else:
            pg.alert(text='ты проиграл')
            pg.alert(text=a, title='твой счет')
    if c == 'свое число':
        w = int(pg.prompt(text='твоя ставка'))
        r = int(pg.prompt(text='твое число(от 1 до 36):'))
        a = a - w
        e = random.randint(1, 36)
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
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    summ = first+second
    pg.alert(title='кости: сумма',text=first + second)
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
    a  -= w
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    summ2 = first+second
    pg.alert(title='кости: сумма 2', text=first + second)
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
    global a
    choice = pg.confirm(title='''*********************ОДНОРУКИЙ БАНДИТ*********************''', text='''
                правила игры:
                1.при совпадении двух чисел ставка не списывается
                2.совпало 3-х2
                3.совпало 4-х5
                4.совпало 5-х10
            ''', buttons=['поехали!', 'выйти'])
    if choice == 'выйти':
        return
    w = int(pg.prompt(text='ставка', title='однорукий бандит', default='100'))
    a -= w
    slot1 = random.randint(3, 9)
    slot2 = random.randint(3, 9)
    slot3 = random.randint(3, 9)
    slot4 = random.randint(3, 9)
    slot5 = random.randint(3, 9)
    pg.alert(title='однорукий бандит: выпало', text=(slot1,slot2,slot3,slot4,slot5))
    r=[slot1,slot2,slot3,slot4,slot5]
    t=Counter(r)
    h=[]
    for i in range(3,10):
        h.append(t[i])
    if max(h) <= 1:
        pg.alert(title='однорукий бандит', text='ты проиграл')
        pg.alert(title='твой счет', text=a)
    elif max(h) == 2:
        a = a + w
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет остался прежним', text=a)
    elif max(h) == 3:
        a = a + w * 2
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет', text=a)
    elif max(h) == 4:
        a = a + w * 5
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет', text=a)
    elif max(h) == 5:
        a = a + w * 10
        pg.alert(title='однорукий бандит', text='ты выиграл')
        pg.alert(title='твой счет', text=a)

def rockPaperScissors():
    global a
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
        pg.alert(title='камень ножници бумага', text='бот выкинул камень')
    elif bot == 2:
        pg.alert(title='камень ножници бумага', text='бот выкинул ножници')
    elif bot == 3:
        pg.alert(title='камень ножници бумага', text='бот выкинул бумагу')
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