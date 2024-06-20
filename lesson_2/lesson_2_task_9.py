# поменять значения var_1 и var_2 местами 
var_1 = 37
var_2 = 99
var3 = var_1 # через переменную
var_1 = var_2
var_2 = var3
print(var_1, var_2, sep=',')

# замена переменных
var_1 = 37
var_2 = 99
var_1, var_2 = var_2, var_1
print(var_1, var_2, sep=',')