field = [[" "] * 3 for i in range(3)]


def hello_instruction():
    print("-ДЗ от yernbekberdiev@gmail.com-")
    print("  Приветствуем вас  ")
    print("       в игре       ")
    print("  крестики-нолики   ")
    print("  формат ввода: x y ")
    print("  x - номер строки  ")
    print("  y - номер столбца ")
    print()


def console_for_player():
    print(f"  | 0 | 1 | 2 |")
    print("  ------------- ")
    for i, row in enumerate(field):
        row_info = f"{i} | {' | '.join(row)} |"
        print(row_info)
        print("  ------------- ")


def ask():
    while True:
        a = input("Введите координаты: ").split()
        if len(a) == 2:
            x, y = a
            if x.isdigit() and y.isdigit():
                x, y = int(x), int(y)
                if 0 <= x <= 2 and 0 <= y <= 2:
                    if field[x][y] == " ":
                        return x, y
                    else:
                        print("Клетка занята")
                else:
                    print("Координаты вне диапазона")
            else:
                print("Введите числа!")
        else:
            print("Ввдите 2 координаты")



def ask_2nd_type():
    while True:
        cord = input("Введите координаты").split()

        if len(cord) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cord

        if not(x.isdigit()) and not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue
        return x, y

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for a in win_cord:
        symbol = []
        for c in a:
            symbol.append(field[c[0]][c[1]])
            if symbol == ["X", "X", "X"]:
                print("Выграл Х")
                return True
            if symbol == ["0", "0", "0"]:
                print("Выграл 0")
                return True
    return False



hello_instruction()
num = 0
while True:
    console_for_player()
    num += 1

    if num % 2 == 1:
        print("Ходит X")
    else:
        print("Ходит 0")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Ничья!")
        break

