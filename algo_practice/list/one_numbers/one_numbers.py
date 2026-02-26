import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 공백이 없게 입력되므로 strip()사용해서 한글자씩 쪼개기
    arr = list(map(int, input().strip()))

    count = 0
    best = 0

    for i in arr:
        if i == 1: # i가 1이면
            count += 1 # count에 1씩 더하기(현재 연속된 1의 길이를 늘림)
            if count > best: # 만약 count가 best보다 크면
                best = count # best 값 갱신
        else :
            count = 0

    print(f'#{tc} {best}')



