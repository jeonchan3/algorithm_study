c = 0
p = 0
a = input()
for j in range(len(a)):
    if a[j] == "(":
        c += 1
    else:
        c -= 1
        if a[j-1] == "(":
            p += c
        else:
            p += 1
print(p)