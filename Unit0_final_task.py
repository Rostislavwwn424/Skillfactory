playing_field = [
    [" ", '0', '1', '2'],
    ["0", '-', '-', '-'],
    ["1", '-', '-', '-'],
    ["2", '-', '-', '-'],
]


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


def end_check():
    move_number = 0



start_game()