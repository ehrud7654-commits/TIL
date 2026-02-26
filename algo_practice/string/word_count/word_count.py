T = int(input())

for tc in range(1, T+1):
    str1 = input() # 찾을 문자 집합
    str2 = input() # 개수를 셀 문자열

    count_dict = {} # {문자: 등장 횟수} 형태로 저장할 딕셔너리, {'A': 3, 'B': 1}

    # str2에서 문자 개수 세기
    for i in str2: # str2의 문자를 하나씩 꺼내서 i에 넣음
        if i in count_dict: # 이미 등장했던 문자면 +1
            count_dict[i] += 1
        else: # 처음 나온 문자면 1로 시작
            count_dict[i] = 1

    # 이 과정을 끝내면 count_dict는 아래같은 빈도표가 됨 (예: str2 = "ABABAC")
    # count_dict = {'A': 3, 'B': 2, 'C': 1}

    # str1 문자들 중 최댓값 찾기
    max_count = 0
    for i in str1: # str1에 있는 문자를 하나씩 보기
        if i in count_dict: # count-dict에 있으면
            max_count = max(max_count, count_dict[i]) # 최댓값 갱신

    print(f'#{tc} {max_count}')


T = int(input())

for tc in range(1, T+1):
    str1 = set(input())
    str2 = list(input())

    max_alpha = 0
    for i in str1:
        max_alpha = max(max_alpha, str2.count(i))

    print(f'#{tc} {max_alpha}')

