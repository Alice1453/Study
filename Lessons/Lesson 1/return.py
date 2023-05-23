# def even(x):
#     return x % 2 == 0
#
# for i in range(1, 11):
#     print(i, even(i))

# def factorial(x):
#     pr = 1
#     for i in range(2, x + 1):
#         pr = pr * i
#     return pr
#
#
# for i in range(1, 8):
#     print(i, factorial(i))

def square_and_perimetr(a, b):
    c = []
    c.append(a * b)
    c.append(2 * (a + b))
    return c

print(square_and_perimetr(2, 6))




# square, perimetr = square_and_perimetr(2, 5)
# print(square, perimetr)

# print(square_and_perimetr(3, 6))
