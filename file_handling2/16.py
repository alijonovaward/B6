import os

old_sub = input("eski sub = ")
new_sub = input("yangi sub = ")

os.rename(old_sub, new_sub)
