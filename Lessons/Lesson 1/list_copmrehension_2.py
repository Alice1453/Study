# n = 7
# m = 3
#
# a = [[0] * m for i in range(n)]
# for i in a:
#     print(i)

# a = [(i,j) for i in "abc" for j in [1, 2, 3]]
# print(a)

a = [i * j for i in [1, 2, 3, 4, 5] for j in [1, 2, 3] if i * j > 10]
print(a)

