n = int(input())
a = input()
s = a.split()
L = []
for x in s:
    L.append(int(x))
L.sort()
x = int(input())
c = 0
left = 0
right = n - 1
while left < right:
    if L[left] + L[right] == x:
        c += 1
        left += 1
        right -= 1
    elif L[left] + L[right] < x:
        left += 1
    else:
        right -= 1
print(c)