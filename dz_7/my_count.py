'''
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
'''

import os
import pickle

file_name_count = 'my_count_pickle.data'
file_name_history = 'history_my_count_pickle.data'

count = 0
history = []
order = []

if os.path.exists(file_name_count):
    with open(file_name_count, 'rb') as f:
        count = pickle.load(f)

if os.path.exists(file_name_history):
    with open(file_name_history, 'rb') as f1:
        history = pickle.load(f1)

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'Баланс: {count}')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        inter = int(input('Введите сумму: '))
        count += inter

    if choice == '2':
        buy_name = input('Введите название: ')
        buy_summ = int(input('Введите цену: '))
        count -= buy_summ
        order = (buy_name, buy_summ)
        history.append(order)

        if buy_summ > count:
            print("На счету недостаточно средств")

    elif choice == '3':
        print(f'Ваши покупки:\n{history}')

    elif choice == '4':
        with open(file_name_count, 'wb') as f:
            pickle.dump(count, f)
        with open(file_name_history, 'wb') as f1:
            pickle.dump(history, f1)
        break
