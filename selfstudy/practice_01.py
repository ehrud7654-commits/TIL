# 16진수 문자로 이루어진 1차 배열, 7비트씩 묶어서 10진수로 변환하기
T = int(input().strip())

for tc in range(1, T + 1):
    N, hex_str = input().split()   # hex_str는 문자열로
    N = int(N)

    answer = []
    for ch in hex_str:
        v = int(ch, 16) # ch 를 16진수로 변환
        answer.append(format(v, '04b')) # v를 4자리 2진수로 변환해서 append

    print(f"#{tc} {''.join(answer)}")