#2675

num = int(input())
ans = []
rep = []
idx = 0
for i in range(num):
    x = input().split(" ")
    R = int(x[0])
    S = x[1]
    rep.append(R)
    ans.append(S)

for i in ans:
    for j in range(len(i)):
        print(i[j] * rep[idx], end="")
    idx += 1
    print()




