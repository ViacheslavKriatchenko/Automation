from address import Address
from mailing import Mailing

to_address = Address(35101, 'Barselona', 'calle Juan', 25, '3C')
from_address = Address(18799, 'Paris', 'Rue Catinat', 56, '46A')

direction = Mailing(
    to_address, from_address, 250, 'RX444172478DE')

print(f'Отправление {direction.track} из {direction.from_address.index}, '
      f'{direction.from_address.city}, {direction.from_address.street}, '
      f'{direction.from_address.house} - {direction.from_address.appartment} '
      f'в {direction.to_address.index}, {direction.to_address.city}, '
      f'{direction.to_address.street}, {direction.to_address.house} - '
      f' {direction.to_address.appartment}.'
      f' Стоимость {direction.cost} рублей.')
