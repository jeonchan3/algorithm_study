"""
N = int(input())
if N == 1:
    print(1)
else:
    for i in range(20):
        if N > 2**i:
            continue
        else:
            print(2**i - 2 * (2**i - N))
            break
"""
"""
2    2
3    2
4    4
5    2
6    4
7    6
8    8
9    2
10   4
11   6
12   8
13   10
14   12
15   14
16   16
"""

N = int(input())
c = list(range(1, N+1))
f = 0
while f < len(c) - 1:
    f += 1
    c.append(c[f])
    f += 1
print(c[f])