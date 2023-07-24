# filter, sorted, map

friends = ['max', 'kate', 'man', 'leo']

result = []
for friend in friends:
    if friend.startswith('m'):
        result.append(friend)

print(result)


def f(x):
    if x.startswith('m'):
        return True
    else:
        return False


result = filter(f, friends)

print(list(result))

# map
friends = ['max', 'kate', 'man', 'leo']

result = []
for friend in friends:
    result.append(friend.upper())

print(result)


def f(x):
    return x.upper()


# map
print(list(map(f, friends)))


def t(x):
    return x.title()


# map
print(list(map(t, friends)))

# sorted
print(sorted(friends))


def f(x):
    return x[-1]


print(sorted(friends, key=f, reverse=True))

# lambda функции
# def f(x):
#     if x.startswith('m'):
#         return True
#     else:
#         return False

result = filter(lambda x: True if x.startswith('m') else False, friends)


# map
print(list(map(lambda x: x.title(), friends)))
print(list(map(lambda x: x.upper(), friends)))

def f(x):
    return x[-1]


print(sorted(friends, key=lambda x: x[-1]))

# Пример с другими именами

friends = ['anna', 'banana', 'max']

# по 1-ой букве
print(sorted(friends))
# сортировка по 1-ой букве и наоборот
print(sorted(friends, reverse=True))
# сортировка по последней букве
print(sorted(friends, key=lambda x: x[-1]))