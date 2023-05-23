# [вираз for val in колекція]
# a = [0 for i in range(5)]
# print(a)
#
# b = [i ** 2 for i in range(7)]
# print(b)
#
# c = [i % 4 for i in range(4, 15)]
# print(c)
#
# d = [i * 5 for i in "hello"]
# print(d)
#
# i = [ord(i) for i in "abcdefg"]
# print(i)

import random

a = [random.randint(-10, 10) for i in range(10)]
print(a)

b = [abs(elem) for elem in a]
print(b)

c = [elem * 2 for elem in a]
print(c)

# [вираз for val in колекція if умова]

d = [elem for elem in a if elem % 2 == 0 and elem % 4 == 0]
print(d)