money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # начальное значение количества месяцев, которое можно прожить

year = list(range(1, 13))  # задаём срок длиной в год с первого месяца

# количество денег на конец первого месяца
money = money_capital + salary - spend

# цикл для рассчёта оставшихся денег и месяца в котором уйдём в минус
for month in year:
    if month > 0:   # рост цен с первого месяца (у нас отсчёт с нулевого)
        spend_month = spend * (increase + 1)
        spend = spend_month     # переприсваеваем траты, так как рост цен динамический
    else:
        spend_month = spend
    total_money = money + salary - spend_month
    money = total_money
    if total_money < spend_month:   # не хватает денег на аренду - останавливаем цикл
        month += 1  # добавляем первый месяц, который в цикле не учтён
        break

print(month)
