import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    r, c = 0, 0

    # 우 -> 하 -> 좌 -> 상
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    d = 0 # 현재 방향 인덱스 => 오른쪽으로

    for num in range(1, N*N+1): # 숫자 채우기 1부터 N**2까지
        arr[r][c] = num
        # 다음 칸 계산
        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 칸으로 가도 되는지 검사 : arr 밖으로 나가는 지, 숫자로 채워져 있는지
        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0 : # 갈 수 없는 칸이면,
            d = (d+1) % 4 # 못가면 방향 바꾸기
            # 방향 바꾸고 다음 칸 계산
            nr = r + dr[d]
            nc = c + dc[d]
        # 다음 칸으로 이동
        r,c = nr, nc

    print(f'#{tc}')
    for row in arr:
        print(*row)
