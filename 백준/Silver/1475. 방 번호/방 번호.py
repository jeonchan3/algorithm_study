num = int(input())
L = []
L2 = []
L.append(num%10)
if(num//10):
    L.append(num//10%10)
if(num//100):
    L.append(num//100%10)
if(num//1000):
    L.append(num//1000%10)
if(num//10000):
    L.append(num//10000%10)
if(num//100000):
    L.append(num//100000%10)
if(num//1000000):
    L.append(num//1000000%10)
L2.append(L.count(0))
L2.append(L.count(1))
L2.append(L.count(2))
L2.append(L.count(3))
L2.append(L.count(4))
L2.append(L.count(5))
L2.append((L.count(6)+L.count(9))//2+(L.count(6)+L.count(9))%2)
L2.append(L.count(7))
L2.append(L.count(8))
print(max(L2))
