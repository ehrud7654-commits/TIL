import sys

sys.stdin = open('input.txt')

# 버블 정렬
# 버블 정렬은 한 번의 반복으로는 하나의 값만 제자리를 찾기 때문에,
# 모든 값을 제자리에 놓으려면 여러 번 반복해야 해서 for문이 두 개다.
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for _ in range(N-1):
        for i in range(N-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    print(f'#{tc}', *arr)

# 선택 정렬

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        min_idx = i
        for j in range(i,N):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f'#{tc}', *arr)

