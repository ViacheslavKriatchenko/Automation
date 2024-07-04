from smartphone import Smartphone

catalog = []
phone_1 = Smartphone('iPhone', '15 Pro Max', '+7909123789456')
phone_2 = Smartphone('Samsung', 'Galaxy S23', '+79181234455')
phone_3 = Smartphone('Google', 'Pixel 7', '+79097788991')
phone_4 = Smartphone('Xiaomi', 'Redmi 12', '+79095555555')
phone_5 = Smartphone('Samsung', 'Galaxy A53', '+79097890000')
catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

# print(len(catalog))
# print(phone_2.model, phone_2.brand, phone_2.number)
# print(Smartphone.__dict__)
# print(phone_4.__dict__)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
