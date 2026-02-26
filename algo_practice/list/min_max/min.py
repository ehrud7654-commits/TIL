T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]
    max_idx = 0
    min_idx = 0

    for i in range(N):
        if max_v <= arr[i]: # 같은 수 일 때, 뒤에 있는 수의 인덱스가 나와야 하므로
            max_v = arr[i]
            max_idx = i
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i

    result = abs(max_idx-min_idx)

    print(f'#{tc} {result}')

