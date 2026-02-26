"""
# 버스 충전 시 (K)만큼 감
# 버스의 종점 (N)만큼 감
# 충전기가 설치된 정류장의 개수(M)

# 최소 몇 번 충전 했을 때 N까지 도달할 수 있는 지 출력
# 못가면 0 출력
# 그리디한 접근 방법으로 가능/불가능 판별

# 정류소(충전)마다 들르면? -> 도달은 가능하나, 최소라는 목표에 어긋남
# K만큼 가면? -> K의 지점에 충전소가 없다면 문제가 된다
# --> greedy 기법
# 가지고 있는 충전 중에서 가장 먼 곳


"""

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 버스 최대 이동 거리(K), 버스 종점(N), 충전소 개수(M)
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split())) #

    stations = [0] * (N+1) # 정류장이 시작되는 곳은 0
    for i in chargers:
        stations[i] = 1

    # 버스 위치
    current_pos = 0
    # 최종 반환 충전횟수
    char_cnt = 0

    # 버스가 종점에 도착할 때 까지 반복(while/for 선택)
    while current_pos < N:
        # 현재 위치를 최대 위치로 바꿀 것, 내 위치 + K
        next_pos = current_pos + K # next_pos: 최대로 내가 이동한 곳

        # 만약 내가 아직도 종점에 도달하지 못했다면,
        if next_pos < N :
            for i in range(next_pos, current_pos, -1):
                # 가장 먼저 발견되는 충전소가 우리가 충전할 수 있는 충전소인데
                # 우리가 greedy 하게 선택할 수 있는 선택이었다.
                if stations[i] == 1:
                    current_pos = i
                    char_cnt += 1
                    break
            # 뒤로 가는 데 current 부터 K까지 범위 내에 충전소가 하나도 없다는 뜻
            else:
                char_cnt = 0 # 종점 도착 불가능
                break
        # 종점 도달달
        else:
            current_pos = next_pos # while loop 탈출 조건
            break

    print(f'#{tc} {char_cnt}')

