from random import randint


def get_unique_list_numbers() -> list[int]:
    unique_numbers = []
    while len(unique_numbers) != 15:
        step_number = randint(-10, 10)
        if step_number in unique_numbers:
            continue
        else:
            unique_numbers.append(step_number)
    return unique_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
