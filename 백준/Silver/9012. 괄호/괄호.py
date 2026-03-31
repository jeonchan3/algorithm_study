N = int(input())
for i in range(N):
    c = 0
    a = input()
    for j in range(len(a)):
        if a[j] == "(":
            c += 1
        else:
            c-= 1
        if c >= 0:
            continue
        else:
            break
    if c == 0:
        print("YES")
    else:
        print("NO")

