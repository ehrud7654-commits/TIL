T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        idx = i
        if i % 2 == 0:
            for j in range(i, N):
                if arr[idx] < arr[j]:
                    idx = j

        else:
            for j in range(i, N):
                if arr[idx] > arr[j]:
                    idx = j

        arr[i], arr[idx] = arr[idx], arr[i]

    print(f'#{tc}', *arr)

































