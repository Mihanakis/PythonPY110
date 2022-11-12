from pprint import pprint


dict_list = [{'bin': bin(n)} | {'dec': n} | {'oct': oct(n)} | {'hex': hex(n)} for n in range(16)]
pprint(dict_list)
