#2530

clock = input().split(" ")

hour = int(clock[0])
minute = int(clock[1])
second = int(clock[2])

timer = int(input())
fin_second = (second + timer) % 60
fin_min = (minute + ((second + timer) // 60)) % 60
fin_hour = hour + (minute + (second + timer) // 60) // 60

if fin_hour < 24:
    print(f'{fin_hour} {fin_min} {fin_second}')
else:
    fin_hour = fin_hour - 24
    print(f'{fin_hour} {fin_min} {fin_second}')