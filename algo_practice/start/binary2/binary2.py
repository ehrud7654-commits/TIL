# 2의 -승을 반복하여 시행하며 계속 빼주는 원리
# 값이 0보다 작아지지 않게 유지하며 시행
# 0이 될 경우에는 결과값이 반환됨
# 12번이 넘어갈 경우에는 overflow가 실행됨

T = int(input())

for tc in range(1, T+1):
    N = float(input())

