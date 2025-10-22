f = open("name.txt", "r")
lst = f.read().split()
f.close()

d = {}

for w in lst:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

print(d)