f = open("name.txt", "r")

lst = f.read().split()
res = lst[0]

for name in lst:
    if len(name) > len(res):
        res = name

print(res)

f.close()