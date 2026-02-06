# 탐욕 알고리즘
# 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을
# 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달하는 방식

# 탐욕 알고리즘을 활용한 Baby-gin

num = 456789 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num // 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 : print('Baby Gin')
else: print('Lose')

