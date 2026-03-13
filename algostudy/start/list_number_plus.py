paper = [[0]*7 for _ in range(2)]
N = 5

t1 = N
for i in range(0,4):
    paper[0][i] = t1
    t1 += 1

t2 = N
for i in range(6,2,-1):
    paper[1][i] = t2
    t2 -= 1

for row in paper:
    print(row)
