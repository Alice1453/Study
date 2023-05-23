# сортування по останній цифрі
a = [12, 33, 45, 94, 956, 63, 65]
a.sort(key=lambda x: x % 10)
print(a)

# сортування по передостанній цифрі
b = [456, 875, 22, 9, 234, 867]
b.sort(key=lambda x: x // 10 % 10)
print(b)


def linear(k, b):
    return lambda x: x * k + b

graf_1 = linear(2, 5)
print(graf_1(5))

graf_2 = linear(-4, 4)
print(graf_2(4))