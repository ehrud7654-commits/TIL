import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    new_lst = []

    for p in prime:
        count = 0
        while N % p == 0:
            N //= p # N을 P로 나누고,
            count += 1 # 갯수 세기
        new_lst.append(count) #

    print(f'#{tc}', *new_lst)





