import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    current_sum = 0
    max_v = 0

    for i in range(N-M+1):
        for j in range(N-M+1):

            current_sum = 0
            for m in range(M):
                for z in range(M):
                    current_sum += arr[i+m][j+z]

            if max_v < current_sum:
                max_v = current_sum

    print(f'#{tc} {max_v}')














