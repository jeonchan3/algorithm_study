n = int(input())
a = input()
s = a.split()
L = []
for x in s:
    L.append(int(x))
v = int(input())
print(L.count(v))