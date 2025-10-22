f = open("name.txt", "r")
lst = f.readlines()
f.close()

f = open("new_name.txt", "a")

for l in lst:
    if l != "\n":
        f.write(l)
f.close()