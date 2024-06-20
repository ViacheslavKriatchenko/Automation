# самый грубый калькулятор )) денег, лет
def bank(x, y):
    for i in range(1, y+1):
        x += 0.1*x
    print(x)

bank(25000,3)