import sys


def enter_size():  # функция проверки ввода размера матрицы на наличие ошибок
    error_size = "Выберите значение для размера поля от 3 до 10:"  # напоминание пользователю о вводе параметров ряда
    print(""""Игра Крестики-Нолики".\nРазмер ряда для победы будет равен размеру поля.""", error_size)
    while True:
        size = [int(number) for number in input().split() if number.isdigit()]
        if size:                            # проверка на пустое поле
            if len(size) > 1:               # проверка на ввод больше одного значения
                print("Ошибка: 'Введено больше одного значения'.", error_size)
                continue
            size = size[0]
            if size in range(3, 11):        # проверка на соответсвие условиям
                return size
        print("Ошибка: 'Введено некорректное значение'.", error_size)


def vision(square, size):  # функция для вывода квадратных матриц
    for row in range(size):
        print(square[(row * size):(size * (row + 1))])


def turn_in_field(line, size):  # функция превращения списка в матрицу
    field=[]
    for row in range(size):
        field.append([])
        for number in line[(row * size):(size * (row + 1))]:
            field[-1].append(number)
    return field

def invert_symbol(enter_val):  # функция для замены 'X' на 1 и '0' на -1
    exit_val = [0] * len(enter_val)
    for index, val in enumerate(enter_val):
        if val == "X":
            exit_val[index] = 1
        elif val == "0":
            exit_val[index] = -1
    return exit_val


def draw_exam(check_draw):  # функция проверки на ничью
    for val in check_draw:
        if val == "_":
            return
    return sys.exit("Никто не победил! Ничья!")


def check_step(check_val, size):  # проверка рядов, столбцов и диагоналей на наличие победы или ничей
    vision(check_val, size)
    invert_matrix = turn_in_field(invert_symbol(check_val), size)
    sum_line = list(map(sum, invert_matrix))
    sum_column = list(map(sum, zip(*invert_matrix)))
    sum_diag1 = sum(invert_matrix[i][size-i-1] for i in range(size))
    sum_diag2 = sum(invert_matrix[i][i] for i in range(size))
    winrate = sum_line + sum_column + [sum_diag1] + [sum_diag2]  # переменная проверки на победу
    for one_of_sum in winrate:
        if one_of_sum == size:
            return sys.exit("Игрок 1 победил! Победили крестики!")
        elif one_of_sum == -size:
            return sys.exit("Игрок 2 победил! Победили нолики!")
    draw_exam(check_val)


def input_exam(matrix, size):  # функция проверки ввода позиции в матрице на наличие ошибок
    error_str = f"Введите значение свободной ячейки от 1 до {size ** 2}:"  # строка ошибки ввода 'X' и '0'
    while True:
        step = [int(number)-1 for number in input().split() if number.isdigit()]
        if step:                            # проверка на пустое поле
            if len(step) > 1:               # проверка на ввод больше одного значения
                print("Ошибка: 'Введено больше одного значения'.", error_str)
                continue
            step = step[0]
            if step in range(size ** 2):    # проверка на позицию в матрице
                if matrix[step] == "_":     # проверка на пустую строку
                    return step
                print("Ошибка: 'Выбранная ячейка занята'.", error_str)
                continue
        print("Ошибка: 'Введено некорректное значение'.", error_str)


def game(matrix, size):
    while True:
        print("Ход первого игрока. Выберите число в котором нужно поставить 'X':")
        step_X = input_exam(matrix, size)
        matrix[step_X] = "X"
        check_step(matrix, size)
        print("Ход второго игрока. Выберите число в котором нужно поставить '0':")
        step_0 = input_exam(matrix, size)
        matrix[step_0] = "0"
        check_step(matrix, size)


def main():
    size = enter_size()
    matrix = ["_"] * size ** 2  # вычисления буду производить в виде ряда
    print(f"""Правила: Игроки по очереди ставят на свободные клетки поля {size}x{size} знаки (один всегда крестики,
    другой всегда нолики). Первый, выстроивший в ряд {size} свои фигуры по вертикали, горизонтали
    или диагонали, выигрывает. Первый ход делает игрок, ставящий крестики. Начинаем.""")
    eximple = list(range(1, (size ** 2) + 1))  # последовательность чисел для справки пользователю
    vision(eximple, size)  # отображаю пример для понимания как предстоит выбирать ячейки
    game(matrix, size)


if __name__ == "__main__":
    main()
