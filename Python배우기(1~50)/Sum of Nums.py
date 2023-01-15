#1789

S = int(input(''))
i = 1
apx = 0
N = 0
while True:
    if S - (apx + i) <= i:
        break
    apx += i
    i += 1
    N += 1

if apx == S:
    print(N)
else:
    print(N+1)
