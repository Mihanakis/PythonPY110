from random import sample
import string

all_symb = string.ascii_uppercase + string.ascii_lowercase + string.digits
list_symb = [symb for symb in all_symb]


def get_random_password(n=8) -> str:
    return "".join(sample(list_symb, n))


print(get_random_password())
