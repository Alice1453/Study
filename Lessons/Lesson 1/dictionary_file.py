s = input()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
for i in sorted(d):
    print(i, d[i])




