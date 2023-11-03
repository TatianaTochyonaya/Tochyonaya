salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Финансовая подушка безопасности

for i in range(months):
        money_capital += spend - salary  # Увеличение подушки безопасности на величину превышения трат над зарплатой
        spend *= 1 + increase  # Ежемесячный рост цен

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
