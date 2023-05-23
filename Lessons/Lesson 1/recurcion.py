# def fact(x):
#     if x == 1:
#         return x
#     return fact(x - 1) * x
#
#
# print(fact(5))


# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0] + "(" + rec(s[1:-1]) + ")" + s[-1]
#
#
# s = input()
# print(rec(s))


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)

    else:
        return power(x, n - 1) * x


x = int(input("Введіть чило"))
n = int(input("Введіть степінь"))
print(power(x, n))
