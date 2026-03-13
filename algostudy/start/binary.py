result = 0b11011110 & 0b11011

print(result) # 26, & 연산(비트 AND)의 결과는 항상 정수
print(bin(result)) # 0b11010

result2 = 0x4A3 | 25

print(result2)
print(bin(result2))

# XOR, 둘 다 1이거나 0인 경우는 0
result3 = 0b1011 ^ 0b1101

print(result3)
print(bin(result3))

# 어떤 값이던 특정 수로 2회 XOR하면 원래 수로 돌아옴(암호화)
# 암호화 프로그램 제작(key = 1004)
encoding = 1000 ^ 1004
decoding = 4 ^ 1004

print(encoding)
print(decoding)

# << 연산
a = 0b1
for _ in range(5):
    print(bin(a), a)
    a = a << 1


# 비트 연산 문제 풀어보기
N = 5
M = 31

if (M & (1 << N) - 1 == (1 << N) - 1):
    print("ON")
else:
    print("OFF")

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





