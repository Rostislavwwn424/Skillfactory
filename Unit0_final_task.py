playing_field = [
    [" ", '0', '1', '2'],
    ["0", '-', '-', '-'],
    ["1", '-', '-', '-'],
    ["2", '-', '-', '-'],
]

move_number = 1
winner = None


def show_field():
    for i in range(4):
        for j in range(4):
            print(playing_field[j][i], end=" ")
        print()


def start_game():
    check_start = None
    print("   Игра «Крестики-нолики»   ")
    print("     формат ввода: x y      ")
    print("     x - номер столбца      ")
    print("     y - номер строки       ")
    while check_start != 'start':
        check_start = input('Для запуска игры введите Start \n')
        check_start = check_start.lower()

    show_field()


def do_move():
    global move_number
    enter_value_split = input(('Крестики' if move_number % 2 else "Нолики") + ' cделайте ход \n').split()
    return enter_value_split[0], enter_value_split[1]


def end_check():
    global winner
    for i in range(1, 4):
        if playing_field[1][i] == playing_field[2][i] == playing_field[3][i] and (playing_field[1][i] != "-"):
            winner = playing_field[1][i]
        elif playing_field[i][1] == playing_field[i][2] == playing_field[i][3] and (playing_field[i][1] != "-"):
            winner = playing_field[i][1]
        elif playing_field[1][1] == playing_field[2][2] == playing_field[3][3] and (playing_field[1][1] != "-"):
            winner = playing_field[1][1]
        elif playing_field[3][1] == playing_field[2][2] == playing_field[1][3] and (playing_field[3][1] != "-"):
            winner = playing_field[3][1]



start_game()

while True:

    x, y = map(int,(do_move()))
    playing_field[x+1][y+1] = "x" if move_number % 2 else "o"
    move_number += 1
    show_field()
    end_check()
    if winner or move_number == 10:
        break

if move_number != 10 or winner:
    print("Игра окончена, победили " + ("крестики" if winner == "x" else "нолики"))
else:
    print("Игра окончена, ничья")