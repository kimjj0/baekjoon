#2558

clock = input().split(" ")

hour = int(clock[0])
min = int(clock[1])

timer = int(input())
fin_min = (min + timer) % 60
fin_hour = hour + ((min + timer) // 60)

if fin_hour < 24:
    print(f'{fin_hour} {fin_min}')
else:
    fin_hour = fin_hour - 24
    print(f'{fin_hour} {fin_min}')