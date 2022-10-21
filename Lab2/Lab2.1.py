src = not False and True or False and not True

# В первую очередь в данном примере выполняется not, затем and и последним or

src_by_the_hand_step1 = True and True or False and False # преобразуем not
src_by_the_hand_step2 = True or False # преобразуем and
src_by_the_hand_step2 = True # преобразуем or

result = not False and True or False and not True

print(src == result)
