# import sys
#
# sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for _ in range(N):
        max_idx = arr.index(max(arr)) # 가장 높은 상자의 인덱스
        min_idx = arr.index(min(arr)) # 가장 낮은 곳의 인덱스

        arr[max_idx] -= 1 # 가장 높은 상자 -1 씩
        arr[min_idx] += 1 # 가장 낮은 상자에 +1 씩

    # 만약 가장 높은 상자와 가장 낮은 곳의 차이가 1이내라면 break
    if arr[max_idx] - arr[min_idx] <= 1:
        break

    # 평탄화 완료 후 가장 높은 상자와 낮은 상자의 차이
    result = max(arr) - min(arr)

    print(f'#{tc} {result}')
