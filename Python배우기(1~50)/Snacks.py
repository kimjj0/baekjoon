#10156

A, B, C = map(int, input().split())
if A * B < C:
    print(0)
else:
    print(A * B - C)