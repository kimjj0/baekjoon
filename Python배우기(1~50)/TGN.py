#5063

result = []
N = int(input())
for i in range(N):
    r, e, c = map(int, input().split())
    if r + c < e:
        result.append('advertise')
    elif r + c > e:
        result.append('do not advertise')
    else:
        result.append('does not matter')

for i in result:
    print(i)