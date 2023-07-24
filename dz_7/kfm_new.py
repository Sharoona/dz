# Консольный файловый менеджер
# - создать папку
# после выбора пользователь вводит название папки, создаем её в рабочей директории;

import shutil
import os
import sys
import pickle

import shutil
import os

new_dir = input("Создать папку.\nВведите название новой папки: ")
os.mkdir(new_dir) if not os.path.exists(new_dir) else None

remove_dir = input("Удалить папку.\nВведите название папки для удаления: ")
os.rmdir(remove_dir) if os.path.exists(remove_dir) else None

name_copy_dir = input("Копирование файла/папки.\nВведите название папки в которой лежит файл: ")
name_copy_file = input("Введите название файла для копирования: ")

shutil.copy(
    os.path.join("..\\", name_copy_dir, name_copy_file),
    os.path.join("\\dz5")
)


# - просмотр содержимого рабочей директории
# вывод всех объектов в рабочей папке;
print("Все папки и файлы:", os.listdir())

# "сохранить содержимое рабочей директории в файл"
# Получаем текущую рабочую директорию
current_directory = os.getcwd()

# Получаем список файлов и папок в текущей директории
content_list = os.listdir(current_directory)

# Имя файла, в который будем сохранять содержимое
file_name = "listdir.txt"

# Открываем файл для записи
with open(file_name, "w") as f:
    # Записываем содержимое в файл
    f.writelines(f"{item}\n" for item in content_list)

print("Содержимое директории сохранено в файл:", file_name)

# - посмотреть только папки
# вывод только папок которые находятся в рабочей папке;
directories = (os.path.join(dirpath, dirname) for dirpath, dirnames in os.walk(".") for dirname in dirnames)

print("Каталоги:")
print(*directories, sep="\n")

# Посмотреть только файлы в рабочей папке
file_paths = [os.path.join(dirpath, filename) for dirpath, _, filenames in os.walk(".") for filename in filenames]
print("Файлы:", *file_paths, sep="\n")

# Просмотр информации об операционной системе
print("Операционная система: ", os.name)

# Вывод информации о создателе программы
current_dir = os.getcwd()
filename = os.path.basename(__file__)
file_stat = os.stat(filename)
uid = file_stat.st_uid
username = pwd.getpwuid(uid).pw_name
print(f'Создатель {filename} в папке {current_dir}: {username}')

# Играть в викторину
os.startfile(r'\\dz6\\victory1.py')

# Мой банковский счет
os.startfile(r'\\my_count.py')

# Смена рабочей директории (*необязательный пункт)
path = input("Введите путь к новой рабочей директории: ")
os.chdir(path)

# Выход
sys.exit()
