import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0 # 파리채의 최대값

    # 파리채 시작 위치 범위
    # 파리채의 왼쪽 위 시작 좌표(i, j)를 가능한 모든 위치로 이동
    # 파리채 크기가 M이므로 시작점은 0 ~ N-M 까지만 가능
    for i in range(N-M+1):
        for j in range(N-M+1):
            current_sum = 0  # 현재 파리채에서의 합, (i, j) 위치에서의 합은 매번 새로 계산해야 함
            # 파리채 영역의 합 구하기
            for m in range(M):
                for z in range(M):
                    current_sum += arr[i+m][j+z] # 파리채 범위에 있는 숫자 모두 더해서 저장

            if max_v < current_sum : # 최대값 갱신
                max_v = current_sum

    print(f'#{tc} {max_v}')














