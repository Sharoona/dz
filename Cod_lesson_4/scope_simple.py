# Области видимости


def f(a, b):
    a = 10
    # ошибки нету
    print(a)


e = 1
f(e, 9999)

# print(e)


a = 1
f(a, 9999)

print(a)
