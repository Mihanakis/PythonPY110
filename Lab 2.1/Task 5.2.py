def task() -> list:
    temp_tuple = (0, 36.6, 100)

    return list(map(lambda t: t * (9 / 5) + 32, temp_tuple))


if __name__ == "__main__":
    print(task())
