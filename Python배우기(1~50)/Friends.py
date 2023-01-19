#5717

total = []
while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    total.append(M + F)

for i in total:
    print(i)