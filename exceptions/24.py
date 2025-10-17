def conv(lst: list):
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except ValueError:
            print("int ga o'girib bo'lmaydi")


l = [1, 3, 4, "5", "a", "4", "b"]

conv(l)

for i in l:
    print(i, type(i))