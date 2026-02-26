import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
num_codes = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T+1):
    test_num, test_len = input().split()
    arr = input().split()

    count_list = [0]*10

    for num in arr:
        idx = num_codes.index(num) # num_codes 리스트에서 num이 몇 번째 인덱스인지 저장
        count_list[idx] += 1

    print(f'#{tc}')
    for i in range(10):
        print((num_codes[i]+' ')*count_list[i], end='')
    print()