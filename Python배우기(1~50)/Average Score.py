#10039

score_arr = []
for i in range(5):
    score = int(input(''))
    if score < 40:
        score = 40
    score_arr.append(score)

print(sum(score_arr)//5)

