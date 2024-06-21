# самый грубый калькулятор )) денег, лет
def bank(x, y):
    for i in range(1, y+1):
        x += 0.1*x
    print('Может быть получите ', round(x, 2))


x, y = int(input('Введите сумму: ')), int(input('Введите кол-во лет: '))
bank(x, y)
