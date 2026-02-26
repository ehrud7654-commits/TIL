import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr_hor = [input() for _ in range(N)]
    arr_ver = ["".join(col) for col in zip(*arr_hor)]
    result = ""

    for board in [arr_hor, arr_ver]:
        for row in board:
            for i in range(N-M+1):
                word = row[i:i+M]
                if word == word[::-1]:
                    result = word
                    break
            if result:
                break
        if result:
            break
    print(f'#{tc} {result}')


    # for row in range(N):
    #     for col in range(N-M+1):
    #         word = arr[row][col:col+M]
    #         if word == word[::-1]:
    #             result = "".join(word)
    #             break
    #     if result:
    #         break
    #
    # for col in range(N):
    #     for row in range(N-M+1):
    #         vertical_word = []
    #         for k in range(M):
    #             vertical_word.append(arr[row+k][col])
    #         if vertical_word == vertical_word[::-1]:
    #             result = "".join(vertical_word)
    #             break
    #     if result:
    #         break
    # print(f'#{tc} {result}')