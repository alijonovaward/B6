s = list(map(int, input().split()))

f = open("even_nums.txt", "w")

for num in s:
    if num % 2 == 0:
        f.write(f"{num} ")

f.close()