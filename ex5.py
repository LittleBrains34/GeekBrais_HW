rev = int(input('Введите выручку вашей организации - '))
cost = int(input('Введите издержки вашей организации - '))
people = int(input('Сколько сотрудников работает в вашей организации - '))
amount = rev - cost
rent = amount / rev * 100

if rev > cost:
    print('Ваша компания в плюсе')
    print(f'рентабельность вашей фирмы составляет {rent} %')
elif rev < 0:
    print('Ваша компания в минусе и не рентабельна')
else:
    print("Ваша компания пока работает без прибыли, но и без убытка")

money = amount / people
print('На одного сотрудника приходится по', money, 'рублей прибыли')