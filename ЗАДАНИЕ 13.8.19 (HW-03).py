tickets = int(input('введите необходимое число билетов:  '))
ages = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст участника {i + 1}:\n'))
    ages.append(input_value)
    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
full_price = sum(map(price, ages))
discount_price = int(full_price * 0.9)
if tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_price, "руб.")
else:
    print('Стоимость всех билетов: ', full_price, "руб.")
    
