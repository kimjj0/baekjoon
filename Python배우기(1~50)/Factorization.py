#11653

N = int(input(""))
for i in range(2, N+1):
    while True:
        if N % i == 0:
            print(i)
            N /= i
        if N % i != 0:
            break

