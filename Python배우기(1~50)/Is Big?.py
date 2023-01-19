#4101

ans = []
while True:
    A, B = map(int, input().split())
    if A > B:
        ans.append('Yes')
    else:
        if A == B == 0:
            break
        ans.append('No')


for i in ans:
    print(i)