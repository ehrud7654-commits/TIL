import sys

sys.stdin = open('input1.txt')

N = int(input()) # 전체 tc 수:1

for tc in range(1, N+1):
    # 상자 칸의 개수
    box_cnt = int(input())
    # 공백을 기준으로 나눠서, 입력을 받은 문자열의 각 값들을
    # 하나하나 int로 형변환
    # list로 형변환
    boxes = list(map(int, input().split())) # 7 4 2 0 0 6 0 7 0