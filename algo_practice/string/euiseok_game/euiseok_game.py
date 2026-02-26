import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    result = []

    # 5개 단어 길이가 서로 다를 수 있으므로 가장 긴 길이 기준으로 읽음
    max_len = max(len(s) for s in arr)

    for col in range(max_len): # 몇 번쩨 문자 위치(열)
        for row in range(5): # 위에서 아래로, 몇 번째 줄
            if col < len(arr[row]): # 문자가 있을 때만 읽음
                result.append(arr[row][col])

    print(f'#{tc} {"".join(result)}')
