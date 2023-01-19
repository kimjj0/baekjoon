#1934

import math

T = int(input())
lcm = []
for i in range(T):
    A, B = input().split()
    lcm.append(math.lcm(int(A), int(B)))

for i in lcm:
    print(i)