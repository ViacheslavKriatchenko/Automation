# lessons_Python_Automation
### 1 Урок:
Типы данных. Понятие переменной  
+ Списки  
+ Функции  
+ Области видимости переменной  
+ Стек вызовов  
  ***Пример:***
```
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
print(f'Вас зовут: {first_name} {last_name}')
```
### 2 Урок:
+ Ветвления. Условные операторы  
+ Циклы  
+ Логические операторы  
  ***Пример:***
```
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst2 = []
for i in range(0, len(lst)):
    if lst[i] < 30 and lst[i] % 3 == 0:
        lst2.append(lst[i])
print(lst2)
```
### 3 Урок:
+ Основные понятия ООП  
+ Методы и поля класса  
+ Взаимодействие классов  
+ Вложенные классы  
  ***Пример***
```
class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('user created')

    def greeting(self):
        print(f'{self.name} says HELLO!')


class Student(Person):

    def __init__(self, name, age, average_grade) -> None:
        super().__init__(name, age)
        self.average_grade = average_grade

    def greeting(self):
        print(f'Student with name {self.name} says HELLO!')
```
### 4 Урок
