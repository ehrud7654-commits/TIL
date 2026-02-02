import sys

sys.stdin = open('input1.txt')

T= int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 현재 값 = 처음 값부터 M까지 더하기
    current_sum = sum(arr[:M])
    # 첫번째 현재 값을 최대값, 최소값으로 설정
    max_sum = current_sum
    min_sum = current_sum

    # 두번째 값부터 더하기
    # i 는 항상 윈도우에 새로 들어오는 숫자의 인덱스
    # 현재 합 = 현재 합 + 새로 들어오는 값 - 빠지는 값
    for i in range(M, N):
        current_sum += arr[i] - arr[i-M]
        if max_sum < current_sum :
            max_sum = current_sum
        elif min_sum > current_sum :
            min_sum = current_sum

    print(f'#{tc} {max_sum - min_sum}')
