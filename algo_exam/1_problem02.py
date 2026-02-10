import sys
sys.stdin = open('input2.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    flies_best = 0
    for r in range(N):
        for c in range(M):
            s = 0
            if arr[r][c] == 0:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr <N and 0 <= nc < M:
                        s += arr[nr][nc]

                if flies_best < s:
                    flies_best = s

    print(f'#{tc} {flies_best}')