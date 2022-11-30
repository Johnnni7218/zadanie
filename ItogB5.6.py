pole = [1, 2, 3,    #игровое поле
        4, 5, 6,
        7, 8, 9]

vik = [[0, 1, 2],    #выигрышные варианты
       [3, 4, 5],
       [6, 7, 8],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [6, 7, 8],
       [2, 4, 6]]

def print_pole():    #функция вывода поля на экран
    print(f"| {pole[0]} | {pole[1]} | {pole[2]} |")
    print("-------------")
    print(f"| {pole[3]} | {pole[4]} | {pole[5]} |")
    print("-------------")
    print(f"| {pole[6]} | {pole[7]} | {pole[8]} |")
    print("              ")
    print("              ")

def step_pole(step, symbol):   #функция замены индекса на символ
    ind = pole.index(step)
    pole[ind] = symbol

#Проверка победы
def pobeda():
    win = ""
    for i in vik:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
         win = "X"
        if pole[i[0]] == "0" and pole[i[1]] == "0" and pole[i[2]] == "0":
         win = "0"
    return win

move = 0  #Основной цикл игры
while move <= 10:
    print_pole()
    win = pobeda()
    if win != "":
        print( f"КОНЕЦ ИГРЫ ПОБЕДИЛИ {win}")
        break
    if move == 9:
        print("КОНЕЦ ИГРЫ")
        print("У ВАС НИЧЬЯ")
        break
    elif move % 2 == 1:
        symbol = 'X'
        step = int(input("Укажите ячейку куда поставить Х - "))
        if step not in pole:
            print ("Укажите правильную клетку")
            continue
    elif move % 2 == 0:
        symbol = '0'
        step = int(input("Укажите ячейку куда поставить 0 - "))
        if step not in pole:
            print ("Укажите правильную клетку")
            continue
    move += 1
    step_pole(step, symbol)

