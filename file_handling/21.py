f = open("name.txt", "r+")

nums = f.read().split()
print(nums)

nums.sort()
f.seek(0)

f.write(" ".join(nums))
