# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#
#     l, r = 0, N - 1 #arr[l] => 최소 , arr[r] => 최대
#     ans = []
#     for i in range(10):
#         if i % 2 == 0: # 짝수 위치면 최대값 순서대로넣기
#             ans.append(arr[r])
#             r -= 1  # 최대
#         else: # 홀수 위치면 최소값 순서대로 넣기
#             ans.append(arr[l])
#             l += 1  # 최소
#
#     print(f"#{tc}", *ans)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(10):
        idx = i # 지금 자리를 채우고 싶은 위치
        if i % 2 == 0: # i가 짝수 자리 이면,
            for j in range(i, N):
                if arr[idx] < arr[j]: # 최댓값 넣기
                    idx = j

        else: # i가 홀수 자리 이면,
            for j in range(i, N):
                if arr[idx] > arr[j]: # 최솟값 넣기
                    idx = j

        arr[i], arr[idx] = arr[idx], arr[i] # 자리 바꾸기

    print(f'#{tc}', *arr[:10])

# 지금 채울 자리(i)를 정한다
#
# 그 자리에 들어갈 값(최대 or 최소)을
#
# 남은 구간에서 찾아서
#
# 그 값이 있는 위치(idx)를 기억했다가
#
# 마지막에 arr[i]와 arr[idx]를 바꾼다