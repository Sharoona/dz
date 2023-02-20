#модуль 1
count = int(input("Введите кол-во элементов: "))
result = []
for i in range(count):
    elem = int(input("Введите число: "))
    result.append(elem)
result.sort()
print("Отсортированный список: ", result)
