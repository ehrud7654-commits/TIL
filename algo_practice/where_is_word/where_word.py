import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N:퍼즐 가로세로 길이, K:단어의 길이
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0 # 정답을 쓸 수 있는 곳의 개수
    # 가로 검사
    for i in range(N):
        count = 0 # 연속된 1의 개수
        for j in range(N):
            if arr[i][j] == 1: # 칸에 1이 있으면,
                count += 1 # 연속 길이를 1 늘림
            # 0이 나오면
            else:
                if count == K: # 지금까지 모은 count 개수랑 단어의 길이 K가 같은지 확인
                    answer += 1 # 맞으면 정답 개수 +1
                count = 0 # 다음 1 연속 구간이 있을 수 있으므로 초기화
        if count == K: # 재검사, 마지막에 1이 나오면 끝에 0이 없어서 검사 불가
            answer += 1

    # 세로 검사
    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K:
            answer += 1

    print(f'#{tc} {answer}')

    T = int(input())

    # for tc in range(1, T + 1):
    #     N, K = map(int, input().split())
    #     arr = [list(map(str, input().split())) for _ in range(N)]
    #     count = 0
    #
    #     for i in arr:
    #         lst = ''.join(i).split('0')
    #         for j in range(len(lst)):
    #             if len(lst[j]) == K:
    #                 count += 1
    #
    #     reverse_arr = list(map(list, zip(*arr)))
    #     # print(reverse_arr)
    #     for i in reverse_arr:
    #         reverse_lst = ''.join(i).split('0')
    #         for j in range(len(reverse_lst)):
    #             if len(reverse_lst[j]) == K:
    #                 count += 1
    #
    #     print(f'#{tc} {count}')