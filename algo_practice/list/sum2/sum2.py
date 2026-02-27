import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]
    max_col_summ = 0
    max_summ = 0
    for row in range(100):
        summ = 0
        col_summ = 0
        for col in range(100):
            summ += numbers[row][col]
            col_summ += numbers[col][row]
        # max_summ = max(max_summ, summ)
        if max_summ < summ :
            max_summ = summ
        if max_col_summ < col_summ:
            max_col_summ = col_summ

    max_dia = 0
    max_dia_t = 0
    for row in range(100):
        max_dia += numbers[row][row]
        max_dia_t += numbers[row][100-row-1]

    print(f'#{tc} {max(max_summ,max_col_summ,max_dia,max_dia_t)}')
