print('begin')


def print_house():
    print('   /\\   ')
    print('  /  \\  ')
    print(' /    \\ ')
    print('/      \\')
    print('-' * 8)
    for i in range(4):
        print('|      |')
    print('-' * 8)


for i in range(3):
    print_house()

# забор
print('/\\' * 10)

print_house()
