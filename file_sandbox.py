f = open("res/test.txt", "r+")
for l in f:
    print(l.strip())
f.close()