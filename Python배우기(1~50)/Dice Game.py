#2476

N = int(input())
price = []
for i in range(N):
    A, B, C = map(int, input().split())
    if A == B == C:
        price.append(10000 + A * 1000)
    elif A == B != C or A == C != B:
        price.append(1000 + A * 100)
    elif B == C != A:
        price.append(1000 + B * 100)
    else:
        price.append(max(A, B, C) * 100)

print(max(price))