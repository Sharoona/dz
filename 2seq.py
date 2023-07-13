#модуль 2
my_list = input("Введите числа через запятую: ")
nums = my_list.split("," and ";" and "/")
new_list = []
for i in nums:
    if nums.count(i) == 1:
        new_list.append(i)
print("Результат: ", new_list)




