#3009

x = []
y = []

for i in range(3):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)

for i in range(3):
    if x.count(x[i]) == 1:
        x4 = x[i]
    if y.count(y[i]) == 1:
        y4 = y[i]

print(x4, y4)
