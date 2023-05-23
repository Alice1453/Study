# a = [
#     ("Ivanov", 1996),
#     ("Petrov", 1987),
#     ("Sidorov", 2000),
#     ("Bukov", 1994),
#     ("Popivich", 2001),
#     ('Glinka', 1998)
# ]
#
# b = [elem[0]  for elem in a if elem[1] >= 2000]
# print(b)

# a = {
#     "Ivanov": {"age": 1996, "hobby": "soccer", "car": "BMW"},
#     "Petrov": {"age": 1987, "hobby": "chess", "car": "Opel"},
#     "Sidorov": {"age": 2000, "hobby": "music", "car": "Fiat"},
#     "Bukov": {"age": 1994, "hobby": "tennis", "car": "Mercedes"},
#     "Popivich": {"age": 2001, "hobby": "swim", "car": "Range Rover"},
#     'Glinka': {"age": 1998, "hobby": "draw", "car": "Audi"}
# }
#
# b = [(elem, a[elem]["car"]) for elem in a if a[elem]["age"] < 2000 and a[elem]["hobby"] == "soccer"]
# print(b)

# s = "dfdg89gfgf657kkgk8456hfg"
# b = [int(i) for i in s if i.isdigit()]
# c = [i for i in s if i.isalpha()]
# print(b)
# print(c)

import random
n = 5
m = 5

a = [[random.randint(1, 10) for j in range(m)]for i in range(n)]
for i in a:
    print(i)
b = [a[i][j] for i in range(n) for j in range(m) if i==j]
c = [a[2][j] for j in range(m)]
d = [a[i][3] for i in range(n)]


print("Main diagonal", b)
print("2 stroka", c)
print("3 stolbec", d)