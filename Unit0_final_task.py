tic = 1
tac = -1


def generate_playing_field(n):
    playing_field_g = [[0] * n for _ in range(n)]
    return playing_field_g


def start_game():
    check_start = None
    print("   Игра «Крестики-нолики»   ")
    print("     формат ввода: x y      ")
    print("     x - номер столбца      ")
    print("     y - номер строки       ")
    while check_start != 'start':
        check_start = input('Для запуска игры введите Start \n')
        check_start = check_start.lower()


start_game()
while True:
    input_field_size = input("Введите размер поля \n")
    if input_field_size.isdigit():
        break

field_size = int(input_field_size)
playing_field = generate_playing_field(field_size)


def show_field(n):
    print("  ", end="")
    print(*range(1, n+1))
    for i in range(n):
        print(i+1, end=" ")
        for j in range(n):
            cur = playing_field[j][i]
            print(("x" if cur == tic else "o")if abs(cur) == 1 else "-", end=" ")
        print()


show_field(field_size)
move_number = 1
winner = None


def do_move(n, p_f):
    global move_number
    while True:
        stop = 1
        enter_value = input(('Крестики' if move_number % 2 else "Нолики") + ' cделайте ход \n')
        enter_value_split = enter_value.split()
        for i in enter_value_split:
            if not i.isdigit():
                stop = 0
            elif int(i) <= 0 or int(i) > int(n):
                stop = 0
        if len(enter_value_split) != 2:
            stop = 0

        if stop and p_f[int(enter_value_split[0])-1][int(enter_value_split[1])-1] == 0:
            break

    return enter_value_split[0], enter_value_split[1]


def end_check(n):
    sum_f_di = 0
    sum_s_di = 0
    for i in range(n):
        sum_f_di += playing_field[i][i]
        sum_s_di += playing_field[i][n-1-i]
    if abs(sum_s_di) == n:
        return sum_s_di

    if abs(sum_f_di) == n:
        return sum_f_di

    for i in range(n):
        if abs(sum(playing_field[i])) == n:
            return sum(playing_field[i])
        elif abs(sum(list(zip(*playing_field))[i])) == n:
            return sum(list(zip(*playing_field))[i])
    return False


while True:
    x, y = map(int, do_move(field_size, playing_field))
    playing_field[x-1][y-1] = tic if move_number % 2 else tac
    move_number += 1
    show_field(field_size)
    winner = end_check(field_size)
    if winner or move_number == field_size**2 + 1:
        break

if move_number != field_size**2 + 1 or winner:
    print("Игра окончена, победили " + ("крестики" if winner == field_size else "нолики"))
else:
    print("Игра окончена, ничья")
