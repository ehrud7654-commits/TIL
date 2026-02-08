import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    new_lst = [] #각 소수가 몇번 나왔는 지 저장할 리스트

    for p in prime:
        count = 0
        while N % p == 0: # N이 p로 나누어떨어지는 동안 나누기(나머지생기는 순간 스탑)
            N //= p # N을 P로 나누고,
            count += 1 # 갯수 세기
        new_lst.append(count) # new_lst에 갯수 저장

    print(f'#{tc}', *new_lst)





