salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

timeline = list(range(months))  # список из 10-ти месяцев (отсчёт с нуля)
wastes = [0] * months   # пустой cписок трат за каждый месяц

# цикл для расчёта трат в текущем месяце и занесение их в список трат
for current_months in timeline:
    if current_months >= 1:     # рост цен со второго месяца (у нас отсчёт с нулевого)
        month_spend = spend * (1 + increase)
        spend = month_spend     # переприсваеваем траты, так как рост цен динамический
    else:
        month_spend = spend
    total_wastes = month_spend - salary
    wastes[current_months] = total_wastes   # заменяем пустые ячейки списка на траты в текущем месяце

need_money = int(sum(wastes))   # суммируем траты в целочисленном виде

print(round(need_money))
