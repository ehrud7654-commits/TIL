T = int(input())

for tc in range(1, T+1):

    N = int(input())

    numbers = input().split('0') # ['','111','','1'] 이런 식으로 문자열 리스트로 입력받음

    max_len = 0
    for num in numbers:
        if len(num) < max_len :
            max_len = len(num)

    print(f'#{tc} {max_len}')

    # T = int(input())
    #
    # for tc in range(1, T + 1):
    #     N = int(input())
    #     # 공백이 없게 입력되므로 strip()사용해서 한글자씩 쪼개기
    #     arr = list(map(int, input().strip()))
    #
    #     # 1의 갯수를 셀 변수 count
    #     count = 0
    #     # 가장 많이 연속된 1의 값 변수 best
    #     best = 0
    #     for i in arr:
    #         if i == 1:  # 1이면,
    #             count += 1  # 갯수세기
    #             if count > best:  # count 가 best 보다 크면,
    #                 best = count  # best 에 count 값을 넣기
    #         else:
    #             count = 0  # i 가 1이외의 다른 수 일땐, 갯수를 세지않음
    #
    #     print(f'#{tc} {best}')
































