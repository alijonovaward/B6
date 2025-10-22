f = open("name.txt", "r")
lines = f.readlines()
f.close()

f = open("new_name.txt", "a")


for l in lines:
    l = l[:-1]
    f.write(l[::-1] + "\n")

f.close()