f = open("name.txt", "r+")
text = f.read()

text = text.replace("ali", "alijon")

f.seek(0)

f.write(text)

f.close()