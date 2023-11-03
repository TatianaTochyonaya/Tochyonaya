money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# Инициализация счетчика месяцев
count_of_months = 0

while money_capital > 0:  # Есть подушка безопасности → нет долгов
    if money_capital + salary < spend:  # Если имеющиеся деньги меньше, чем расходы, цикл завершается
        break
    count_of_months += 1
    spend *= 1 + increase  # Ежемесячный рост цен
    money_capital -= spend - salary  # Деньги, которые остались после расходов

print("Количество месяцев, которое можно протянуть без долгов:", count_of_months)
