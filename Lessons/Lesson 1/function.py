# def say_hello():
#     print("Hello")
#     print("everyone")
#
# say_hello()

def square(x):
    print("Квадрат числа", x, "=", x ** 2)


def multiplay(a, b):
    print(a * b)


def even(a):
    if a % 2 == 0:
        print(a, "chetnoe")
    else:
        print(a, "nechetnoe")


def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(pr)

factorial(4)
# for i in range(20, 31):
#     even(i)

# multiplay(4, 10)
#
# for i in range(1, 11):
#     square(i)
