t = int(input())

for i in range(t):
    ans = []
    n = int(input())
    p = 0
    iss = True
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for j in range(n):
        if a[j] == b[j]:
            continue
        if a[j] > b[j]:
            iss = False

        for k in range(n):
            if k == j:
                continue
            if a[j] < a[k] and a[k] >= b[j]:
                a[j] = a[k]
                p += 1
                ans.append([k + 1, j + 1])
                break

    if not iss or p > n:
        print(f"Case #{i + 1}: {-1}")
    else:
        print(f"Case #{i + 1}: {p}")
        for l in ans:
            print(l[0], l[1])
