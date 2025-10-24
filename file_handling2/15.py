import os

sub = "files"

os.chdir(sub)

print(os.getcwd())

with open("name.txt", "w") as f:
    f.write("Aziz")

print(os.path.exists("name.txt"))