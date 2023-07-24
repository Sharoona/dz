# Передача функции в функцию

def print_who(name):
    print(name)


print_who('Max')

p = print_who('Max')
print_who(p)

p = print_who

print(p)
print(type(p))

p('Leo')


def other(name, func):
    # вызов переданной функции внутри другой функции
    func(name)


other('Kate', print_who)


def print_namex5(name):
    print(name * 5)


other('Max', print_namex5)
