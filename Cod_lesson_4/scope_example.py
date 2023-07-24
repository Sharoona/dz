"""
Области видимости
"""
a = 1


def first():
    b = 1

    def second():
        d = 1

        def inner():
            e = 1
            d = 10

        inner()
        print(d)

    second()


first()
