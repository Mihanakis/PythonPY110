import sys

eximple = list(range(1, 10))    # последовательность чисел в которой буду работать

print("""Игра "Крестики-Нолики". Правила: Игроки по очереди ставят на свободные клетки поля 3×3 знаки
 (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали, 
 горизонтали или диагонали, выигрывает. Первый ход делает игрок, ставящий крестики. Начинаем.""")

def vision(square):     # функция для вывода матриц 3x3
    return print(square[0:3], square[3:6], square[6:9], sep="\n")

vision(eximple)         # отображаю пример для понимания как предстоит выбирать ячейки

matrix = ["_"] * 9      # вычисления буду производить в виде ряда

error_str = "Введите корректное значение свободной ячейки от 1 до 9:"

def invert_symbol(enter_val):   # функция для замены 'X' на 1 и '0' на -1
    exit_val = [0] * len(enter_val)
    for index, val in enumerate(enter_val):
        if val == "X":
            exit_val[index] = 1
        elif val == "0":
            exit_val[index] = -1
    return exit_val

def drow_exam(check_draw):  # функция проверки на ничью
    for val in check_draw:
        if val == "_":
            return
    return sys.exit("Никто не победил! Ничья!")

def check_step(check_val):  # проверка рядов, столбцов и диагоналей на наличие победы
    vision(check_val)
    drow_exam(check_val)
    invert_matrix = invert_symbol(check_val)

    sum_1line = sum(invert_matrix[0:3])
    sum_2line = sum(invert_matrix[3:6])
    sum_3line = sum(invert_matrix[6:9])

    sum_1column = invert_matrix[0] + invert_matrix[3] + invert_matrix[6]
    sum_2column = invert_matrix[1] + invert_matrix[4] + invert_matrix[7]
    sum_3column = invert_matrix[2] + invert_matrix[5] + invert_matrix[8]

    sum_1diag = invert_matrix[0] + invert_matrix[4] + invert_matrix[8]
    sum_2diag = invert_matrix[2] + invert_matrix[4] + invert_matrix[6]

    # переменная для которой, если одно из значений принимает значение 3 или -3 - наступает победа
    winrate = [sum_1line, sum_2line, sum_3line, sum_1column, sum_2column, sum_3column, sum_1diag, sum_2diag]
    for one_of_sum in winrate:
        if one_of_sum == 3:
            return sys.exit("Игрок 1 победил! Победили крестики!")
        elif one_of_sum == -3:
            return sys.exit("Игрок 2 победил! Победили нолики!")

def input_exam(step):   # проверка на правильность ввода данных
    while matrix[step] != "_":
        print(error_str)
        step = int(input()) - 1
    return step

def game():
    while True:
        print("Ход первого игрока. Выберите число в котором нужно поставить 'X':")
        step_X = input_exam(int(input())-1)
        matrix[step_X] = "X"
        check_step(matrix)
        print("Ход второго игрока. Выберете число в котором нужно поставить '0':")
        step_0 = input_exam(int(input())-1)
        matrix[step_0] = "0"
        check_step(matrix)

game()
