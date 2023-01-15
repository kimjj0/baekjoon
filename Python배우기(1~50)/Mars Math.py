#5355

T = int(input())
x = 0
ans = []
while x < T:
    mars_math = input().split(" ")
    first_num = float(mars_math[0])
    for i in mars_math:
        if i == '@':
            first_num *= 3
        elif i == '%':
            first_num += 5
        elif i == '#':
            first_num -= 7
    ans.append(first_num)
    x += 1

for i in ans:
    print('{:.2f}'.format(i))