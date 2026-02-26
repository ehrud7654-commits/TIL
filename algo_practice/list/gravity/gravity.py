import sys

sys.stdin = open('input.txt')

T = int(input()) # 전체 tc 수:1

for tc in range(1, T+1):
    # 상자 칸의 개수(가로 칸수)
    box_cnt = int(input())
    # 공백을 기준으로 나눠서, 입력을 받은 문자열의 각 값들을
    # 하나하나 int로 형변환
    # list로 형변환
    box = list(map(int, input().split())) # 7 4 2 0 0 6 0 7 0

    max_v = 0 # 최대 낙차
    for i in range(box_cnt - 1): # 마지막 열은 오른쪽이 없으므로 -1
        cnt = 0  # i박스 오른쪽(i+1~N-1)에 더 낮은 박스 개수 (낙차)
        for j in range(i + 1, box_cnt):
            if box[i] > box[j]:
                cnt += 1  # 더 낮은 박스면 낙차 추가
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')




