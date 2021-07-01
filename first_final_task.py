playing_field = [
    [" ", '0', '1', '2'],
    ["0", '-', '-', '-'],
    ["1", '-', '-', '-'],
    ["2", '-', '-', '-'],
]
check_start = None
winner = None
end_check = 1

while check_start != 'start':
    check_start = input('Для запуска игры «Крестики-нолики» введите Start \n')
    check_start = check_start.lower()

if check_start.lower() == 'start':
    for i in range(4):
        for j in range(4):
            print(playing_field[j][i], end=" ")
        print()

move_number = 0

while end_check:
    if move_number % 2 == 0:
        print('Сейчас ходят крестики, сделайте ход в формате № столбца № строчки')
    else:
        print('Сейчас ходят нолики, сделайте ход в формате № столбца № строчки')
    enter_value_split = input('').split()
    while len(enter_value_split) != 2:
        enter_value_split = input('Введите информацию о ходе в формате № столбца № строчки \n').split()

    x, y = map(int, enter_value_split)

    move_number += 1

    playing_field[x + 1][y + 1] = 'x' if move_number % 2 == 1 else 'o'
    for i in range(4):
        for j in range(4):
            print(playing_field[j][i], end=" ")
        print()

    for i in range(1, 4):
        if playing_field[1][i] == playing_field[2][i] == playing_field[3][i] and (playing_field[1][i] == "x" or playing_field[1][i] == "o"):
            end_check = 0
            winner = playing_field[1][i]
        elif playing_field[i][1] == playing_field[i][2] == playing_field[i][3] and (playing_field[i][1] == "x" or playing_field[i][1] == "o"):
            end_check = 0
            winner = playing_field[i][1]
        elif playing_field[1][1] == playing_field[2][2] == playing_field[3][3] and (playing_field[1][1] == "x" or playing_field[1][1] == "o"):
            end_check = 0
            winner = playing_field[1][1]
        elif playing_field[3][1] == playing_field[2][2] == playing_field[1][3] and (playing_field[3][1] == "x" or playing_field[3][1] == "o"):
            end_check = 0
            winner = playing_field[3][1]

print("Игра окончена, победили " + "крестики" if winner == "x" else "нолики")
