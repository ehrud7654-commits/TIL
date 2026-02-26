T = int(input())

for tc in range(1, T+1):
    str1 = set(input())
    str2 = list(input())

    max_alpha = 0
    for i in str1:
        max_alpha = max(max_alpha, str2.count(i))

    print(f'#{tc} {max_alpha}')



