T = 10

for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    good_view_result = 0
    for i in range(2, N-2):

        left1 = buildings[i-2]
        left2 = buildings[i-1]
        right1 = buildings[i+1]
        right2 = buildings[i+2]

        max_building = max(left1,left2,right1,right2) # 현재 건물 주변 -2,+2 중 가장 높은 건물 조사

        if max_building < buildings[i]: # 주변에서 가장 높은 건물보다 현재 건물이 더 높다면,(조망권 확보)
            good_view_result += buildings[i] - max_building # 현재 건물 - 주변 중 가장 높은 건물 = 조망권 확보 세대수를 결과에 더함

    print(f'#{tc} {good_view_result}')


    # result = 0
    # for i in range(2, N-2): # 왼쪽 두 빌딩, 오른쪽 두 빌딩은 어차피 조망권 확보 x
    #     # 현재 조사 대상(i)의 높이 => 최대 조망권
    #     tmp = buildings[i]
    #
    #     for j in range(i-2, i+3) : # 좌우 4칸씩 조사
    #         # 1. 검사 대상이 나라면, pass(continue)
    #         if i == j:
    #             continue
    #         # 2. 조사 대상이 양 옆보다 더 크고,
    #         # 이 둘의 차이가 최대 조망권보다 작으면,
    #         if buildings[i] > buildings[j] and tmp > buildings[i] - buildings[j] :
    #             tmp = buildings[i] - buildings[j]
    #         # 만약에 조사 대상군 중에서,
    #         # 키가 같거나 큰 건물이 한 번이라도 있으면
    #         elif buildings[i] <= buildings[j] :
    #             break
    #
    #     else:
    #         # i번째 건물 조망권 크기 더하기
    #         result += tmp
    #
    #
    #
    #
    # print(f'#{tc} {result}')
