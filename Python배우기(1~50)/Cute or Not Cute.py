#10886

N = int(input())
result = []
for i in range(N):
    result.append(int(input()))

if result.count(0) > result.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')