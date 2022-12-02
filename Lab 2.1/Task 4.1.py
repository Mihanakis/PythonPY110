from itertools import count


def task():
    counter = count(100, 10)

    for n in range(10):
        print(next(counter))


if __name__ == "__main__":
    task()
