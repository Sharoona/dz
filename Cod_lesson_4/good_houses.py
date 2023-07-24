def print_roof():
    print('   /\\   ')
    print('  /  \\  ')
    print(' /    \\ ')
    print('/      \\')


def print_rectangle(height, wall_symbol='|'):
    print('-' * 8)
    for i in range(height):
        print(f'{wall_symbol}      {wall_symbol}')
    print('-' * 8)


def print_house(height, wall_symbol='|'):
    print_roof()
    print_rectangle(height, wall_symbol)


# Передача параметров по порядку
print_house(4, '#')
print_house(2)
print_house(1, '=')

print_rectangle(4)

# Передача параметров по имени
print_house(wall_symbol='*', height=5)

print_roof()
