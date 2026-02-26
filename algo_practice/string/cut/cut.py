import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stick = input()

    total_stick = 0 # 잘려진 쇠막대기 조각의 총 개수
    stick_count = 0 # 막대기 수 세기

    for i in range(len(stick)):
        if stick[i] == '(': # i == '('이면 막대기 수 +1
            stick_count += 1
        else: # i == ')' 이면
            stick_count -= 1
            if stick[i-1] == '(': # () 이므로 레이저 -> 현재까지 잘린 막대기를 총 막대기 수에 추가
                total_stick += stick_count
            else: # 레이저가 아니라면, 막대기의 끝 -> 막대의 마지막 조각 +1
                total_stick += 1

    print(f'#{tc} {total_stick}')
