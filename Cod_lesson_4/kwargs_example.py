def my_functions(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k)
        print(v)


my_functions(name='Leo', age=10)
my_functions(name='Leo', age=10, is_man=True)
my_functions(name='Leo', is_man=True, age=10)
my_functions(name='Leo')
my_functions()


def print_megafunctions(first, second='2', *args, **kwargs):
    print(first)
    print(second)
    print(args)
    print(kwargs)


print_megafunctions(1, 20, 3, 'string', 5, name='1', age='2')
