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