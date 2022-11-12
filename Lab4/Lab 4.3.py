from random import sample
import string

all_symb = string.ascii_uppercase + string.ascii_lowercase + string.digits

def get_random_password(n=8) -> str:
    return "".join(sample(all_symb, n))


print(get_random_password())
