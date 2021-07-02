import numpy as np
import math


def game_core_v3(number):
    """Сначала устанавливаем любое random число, возможно лучше начинать с n/2(в нашем случае 50), но я не заметил
        прироста в скорости, потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
        Уменьшение и увеличение происходит на половину от разницы самых близких значений сверху и снизу о которых
        нам известно.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    past_predict_h = 100  # Изначально самое близкое значение сверху о котором нам известно - это 100
    past_predict_l = 0  # Изначально самое близкое значение снизу о котором нам известно - это 0
    while number != predict:
        count += 1  # Увеличиваем число попыток на 1 каждый раз когда number != predict
        if number > predict:
            past_predict_l = predict  # Новое самое близкое значение снизу
            predict += math.ceil((past_predict_h - predict) / 2)

        elif number < predict:
            past_predict_h = predict  # Новое самое близкое значение сверху
            predict -= math.ceil((predict - past_predict_l) / 2)

    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
