my_age = input()
print(type(my_age))  # str
print('Ваш возраст ', my_age)  # str
my_age = my_age + 1  # переменная с типом строка + число = ошибка
print('Ваш возраст ', my_age)  # ошибка

# преобразовать тип данных при вводе
my_age = int(input('Введите свой возраст: '))
my_age = my_age + 1
print(f'Ваш возраст: {my_age}')
