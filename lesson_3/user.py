class User:

    def __init__(self, name: str, surname: str) -> None:
        self.name: str = name
        self.surname: str = surname

    def show_name(self):
        print(f'Имя - {self.name}')

    def show_surname(self):
        print(f'Фамилия - {self.surname}')

    def show_name_surname(self):  # печать имя и фамилия
        print(f'Имя - {self.name}, Фамилия - {self.surname}')


# p1 = User('Ivan', 'Ivanov')
# p1.show_name_surname()
