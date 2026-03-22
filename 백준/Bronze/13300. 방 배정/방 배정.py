import math

a = input()
La = a.split()
N = int(La[0])
K = int(La[1])
f = [0,0,0,0,0,0]
m = [0,0,0,0,0,0]
for i in range(N):
    b = input()
    Lb = b.split()
    S = int(Lb[0])
    Y = int(Lb[1]) 
    if S == 0:
        f[Y-1] += 1
    else:
        m[Y-1] += 1
r = 0
for j in range(6):
    r += math.ceil(f[j]/K)
    r += math.ceil(m[j]/K)

print(r)