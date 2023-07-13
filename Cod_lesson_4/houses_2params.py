def print_house(height, wall_symbol='|'):
    print('   /\\   ')
    print('  /  \\  ')
    print(' /    \\ ')
    print('/      \\')
    print('-' * 8)
    for i in range(height):
        print(f'{wall_symbol}      {wall_symbol}')
    print('-' * 8)


# Передача параметров по порядку
print_house(4, '#')
print_house(2)
print_house(1, '=')

# Передача параметров по имени
print_house(wall_symbol='*', height=5)
