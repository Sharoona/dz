#модуль 3

list_1 = input("Введите числа 1-го списка через запятую: ")
nums_1 = list_1.split(",")
list_2 = input("Введите числа 2-го списка через запятую: ")
nums_2 = list_2.split(",")
for i in nums_2:
    if i in nums_1:
        nums_1.remove(i)

print('Результат вычитания 2 из 1 списка: ', nums_1)



