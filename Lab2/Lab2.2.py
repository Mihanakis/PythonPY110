list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_positive_number = list_numbers[0]   # первое значение для поиска максимума

position_positive = 0   # начальный индекс нахождения в списке максимума

# цикл для нахождения индекса и значения максимума:
for position_high, number_high in enumerate(list_numbers):
    if number_high > max_positive_number:
        max_positive_number = number_high
        position_positive = position_high

# меняем максимум и последний элемент:
list_numbers[position_positive] = list_numbers[position_high]
list_numbers[position_high] = max_positive_number

print(list_numbers)
