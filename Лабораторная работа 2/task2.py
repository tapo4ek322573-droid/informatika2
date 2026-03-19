salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Подушка безопасности
month = months # Остаток месяцев
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while month != 0:
    money_capital = money_capital + salary - spend
    spend = spend * (1 + increase) #Расходы
    month -= 1
money_capitall = int (money_capital) #
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", -money_capitall)
