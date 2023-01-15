#2914

i = input("").split(" ")
song_num = int(i[0])
average = int(i[1])

least_num = song_num * (average - 1) + 1
print(least_num)