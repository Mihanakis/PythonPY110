from pprint import pprint


dict_list = []
for n in range(16):
    dict_list += [{'bin': bin(n)} | {'dec': n} | {'oct': oct(n)} | {'hex': hex(n)}]
pprint(dict_list)
