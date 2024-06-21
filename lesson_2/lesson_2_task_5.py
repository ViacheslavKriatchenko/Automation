def month_to_season(month):
    if month <= 0 or month > 12:
        return "Такого времени года не существует, введите число от 1 до 12"
    elif month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"


month = int(input('Введите цифру месяца: '))
season = month_to_season(month)
print(f'Время года - {season}')
