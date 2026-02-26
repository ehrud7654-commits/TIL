import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    max_val = numbers[0]
    min_val = numbers[0]
    max_idx = 0
    min_idx = 0

    for i in range(N):
        if max_val <= numbers[i]:
            max_val = numbers[i]
            max_idx = i

        if min_val > numbers[i]:
            min_val = numbers[i]
            min_idx = i

    result = abs(max_idx - min_idx)

    print(f'#{tc} {result}')

