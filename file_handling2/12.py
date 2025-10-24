import os

sub = "shahriyor2"

if not os.path.exists(sub):
    os.mkdir(sub)

os.chdir(sub)

print(os.getcwd())