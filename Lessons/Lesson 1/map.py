# map(func, *iterables)
# приміняє задану функцію для заданих ітерабельних обєктів
# a = [-1, -2, -3, -4, -5]
# b = list(map(abs, a))
# print(b)

# def f(x):
#     return x ** 2
#
# b = list(map(f, a))
# print(b)

# c = ["hello", "good morning", "abrakadabra"]
# d = list(map(len, c))
# e = list(map(str.upper, c))
# # f = [i[::-1] for i in c]
# f = list(map(lambda x: x[::-1], c))
# print(d)
# print(e)
# print(f)

s = list(map(int, input().split()))
print(s)