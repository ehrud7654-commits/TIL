import sys

sys.stdin = open('input.txt')

T = 3

for tc in range(1, T+1):
    # 건물의 개수
    N = int(input())
    # 공백을 기준으로 나눠서, 입력을 받은 문자열의 각 값들을
    # 하나하나 int로 형변환
    # list로 형변환
    # 건물의 높이 리스트
    buildings = list(map(int, input().split())) # 7 4 2 0 0 6 0 7 0

    result = 0
    for i in range(2, N-2): # 왼쪽 두 빌딩, 오른쪽 두 빌딩은 어차피 조망권 확보 x

        left1 = buildings[i-1]
        left2 = buildings[i-2]
        right1 = buildings[i+1]
        right2 = buildings[i+2]

        max_around = max(left1, left2, right1, right2)

        if buildings[i] > max_around:
            result += buildings[i] - max_around


    print(f'#{tc} {result}')
