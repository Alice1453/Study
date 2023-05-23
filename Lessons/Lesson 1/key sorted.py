def f(x):
    return x % 10

a = [4, 0, 14, 44, 54, 42, 567, 211, 75]
print(sorted(a, key=f, reverse=True))
