
def print_house(wall_symbol='|'):
    print('   /\\   ')
    print('  /  \\  ')
    print(' /    \\ ')
    print('/      \\')
    print('-' * 8)
    for i in range(4):
        print(f'{wall_symbol}      {wall_symbol}')
    print('-' * 8)


for i in range(3):
    print_house('#')

# забор
print('/\\' * 10)

print_house()
print_house('#')
