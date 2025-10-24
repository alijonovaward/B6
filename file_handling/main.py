n = int(input("n = "))
lst = []
ans = 0

for i in range(n):
    k = int(input(f"{i + 1} - sonni kiriting = "))
    if i == 0:
        ans = k

    if ans < k:
        ans = k

print(f"Eng katta son : {ans}")
