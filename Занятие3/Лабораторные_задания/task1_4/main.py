INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r") as input_file:  # открываем входной файл для чтения
        with open(OUTPUT_FILE, "w") as output_file:  # открываем выходной файл для записи
            for upper_line in map(str.upper, input_file):  # поднимаем символы построчно во входном файле
                output_file.write(upper_line)  # записываем полученные строки в выходной файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
