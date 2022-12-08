def min_len_check(fn):
    def wrapper(str_arg):
        if len(str_arg) < 10:
            raise ValueError("Строка слишком короткая")

        return fn(str_arg)

    return wrapper


@min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
