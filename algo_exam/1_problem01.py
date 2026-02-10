T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_a = input()
    arr_b = input()

    idx = 0
    result = -1
    for i in range(N):
        if arr_b[idx] == arr_a[i]:
            idx += 1
            if idx == M:
                result = i
                break

    print(f'#{tc} {result}')