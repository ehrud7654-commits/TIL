import sys
sys.stdin = open("input.txt")

def binary_search(P, key): # P: 전체 쪽수, key: 찾아야 하는 값
    l = 1
    r = P # 전체 쪽수
    count = 0

    while l <= r:
        count += 1 # 책 펼치는 횟수 +1
        middle = (l + r) // 2

        if middle == key:
            return count
        elif middle > key:
            r = middle - 1
        else:
            l = middle + 1

T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    a_count = binary_search(P, Pa)
    b_count = binary_search(P, Pb)

    if a_count < b_count:
        answer = "A"
    elif b_count < a_count:
        answer = "B"
    else:
        answer = "0"

    print(f"#{tc} {answer}")


