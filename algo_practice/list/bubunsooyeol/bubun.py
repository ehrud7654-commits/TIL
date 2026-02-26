T= int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    j = 0 # 수열 B에서 다음으로 맞춰야 할 원소의 인덱스
    for i in range(N): # 수열 A를 왼쪽부터 끝까지 훑는 인덱스
         if i == arr_b[j]: #B의 j번째 원소를 A에서 찾았으면,
             j += 1 #다음 원소(j+1번째)를 찾으러 이동
             if j == M: #B의 길이가 M이니까, j == M이면 B의 0~M-1까지를 전부 찾았다는 뜻
                 break

    if j == M:
        print(f'#{tc} YES')
    else :
        print(f'#{tc} NO')


    # j = 0  # B 포인터
    # for x in arr_a:
    #     if j < M and x == arr_b[j]:
    #         j += 1