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
        if i == 1:
            count += 1
            if count > best :
                best = count
        else :
            count = 0

    print(f'#{tc} {best}')



