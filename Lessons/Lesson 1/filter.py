# filter (func or none, iterable)
# функція перевіряє на тру і фолс кожен ітерабельний елмент

# def f(x):
#     return x > 10
#
#
# a = [14, 2, 44, 56, 23, 5, 123, 7, 76]
# b = list(filter(f, a))
# print(b)

a = {
    "Kyiv": 900,
    "Lviv": 800,
    "Dnipro": 900,
    "Kherson": 600,
    "Lusk": 100,
    "Rivne": 300
}

b = list(filter(lambda x: a[x] > 500, a))
print(b)