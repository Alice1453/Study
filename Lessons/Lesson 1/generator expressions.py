# вираз-генератор відрізняється ДУжками від генератора списків
# можна обходити лише раз
# менше памяті
# c = (i for i in range(1000000000))
# for i in c:
#     print(i)

# def genf():
#     for i in [31, 44, 52]:
#         yield i

# s = genf()
#
# print(next(s))
# print(next(s))
#
# for i in genf():
#     print(i)

def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr

# s = fact(10)
# print(next(s))
# print(next(s))
# print(next(s))

for i in fact(10):
    print(i, end=" ")