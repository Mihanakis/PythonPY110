import json


def task() -> str:
    dict_numbers = {n : n ** 2 for n in range(1, 11)} # формируем словарь
    return json.dumps(dict_numbers, indent=4)  # записываем данные в JSON с отступом 4 символа


if __name__ == "__main__":
    print(task())
