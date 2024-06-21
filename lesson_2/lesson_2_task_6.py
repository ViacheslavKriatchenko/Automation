lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst2 = []
for i in range(0, len(lst)):
    if lst[i] < 30 and lst[i] % 3 == 0:
        lst2.append(lst[i])
print(lst2)
