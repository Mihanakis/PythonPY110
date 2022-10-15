list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

sum_uniq = sum(list_)
numb_uniq = len(set(list_))
middlesum = round(sum_uniq / numb_uniq, 5)

print(sum_uniq)
print(numb_uniq)
print(middlesum)
