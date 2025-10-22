f = open("name.txt", "r")
lines = f.readlines()
f.close()

special = input("word: ")

f = open("sp.txt", "a")


for l in lines:
    if special in l:
        f.write(l)

f.close()