import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    #최댓값 저장 변수
    max_v = 0
    #모든 칸을 시작점으로 검사 -
    for i in range(N): # 모든 칸 (i, j)를 하나씩 다 검사
        for j in range(M):
            # 자기 자신 arr[i][j] 포함
            # 상/하/좌/우 방향으로 1칸부터 arr[i][j]칸까지 있는 칸들의 값 합
            s = arr[i][j]

            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]: # 상하좌우
                # arr[i][j]가 k라면, 거리 1칸, 2칸, …,
                # k칸까지 검사해야 하니까
                # c가 1부터 k까지 돈다.
                for c in range(1, arr[i][j]+1):
                    # 시작점 (i,j)에서 방향(di, dj)로 c칸 이동한 위치가 (ni, nj)
                    ni = i + di * c
                    nj = j + dj * c
                    # ni, nj 가 격자 범위 안이면
                    if 0 <= ni < N and 0 <= nj < M :
                        s += arr[ni][nj] #그 칸의 꽃가루를 s에 더해줘
                    else: # 격자를 벗어나면, 그 방향으로는 더 갈수 없으므로
                        break # 끝내

            if max_v < s:
                max_v = s # 최고 값 갱신

    print(f'#{tc} {max_v}')

