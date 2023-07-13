a = 1


def f(b):
    global a  #
    a = 10


f(0)
print(a)
