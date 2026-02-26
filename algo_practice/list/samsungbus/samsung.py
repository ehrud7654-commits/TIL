T = int(input())

for tc in range(1, T+1):
    N = int(input()) #버스 노선의 개수
    count = [0] * 5002 # 각 정류장을 지나는 노선 수를 저장할 리스트

    # N개의 버스 노선 정보 입력
    for stop in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1): # 해당 구간의 모든 정류장(A부터 B까지)에 대해
            count[i] += 1 # 지나가는 노선 수 증가

        # 질문할 정류장 개수
        P = int(input())
        result = [] # 질문 정류장의 결과를 담을 리스트
        for _ in range(P):
            C = int(input()) # 정류장 번호 입력
            result.append(count[C]) # 해당 정류장을 지나는 노선 수 저장

        print(f'#{tc}', *result)


# T= int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     bus_stop = [0] * 5002
#
#     for _ in range(N):
#         A, B = map(int, input().split())
#         bus_stop[A] += 1 # A정류장부터 +1
#         bus_stop[B+1] -= 1 # B+1정류장부터 노선 -1
#
#     cnt = [0] * 5002
#     running = 0 # 현재 정류장까지 살아있는 노선 수
#     for stop in range(1, 5001):
#         # stop번 정류장에서 새로 시작하는 노선과(+1),
#         # stop번 정류장에서 끝나는 노선(-1) -> 현재 지나가는 버스 개수 갱신
#         running += bus_stop[stop]
#         cnt[stop] = running # stop번 정류장을 지나는 버스 개수 결과를 저장
#
#     P = int(input())
#     answer = []
#     for _ in range(P):
#         C = int(input())
#         answer.append(cnt[C]) #C번 정류장을 지나는 버스 개수를 answer에 append
#
#     print(f'#{tc}', *answer)





