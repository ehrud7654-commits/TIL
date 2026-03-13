arr = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]

r,c = 1,1
N, M = 4,4

dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,-1,1,-1,1]

for i in range(8):
    nr = r + dr[i]
    nc = c + dc[i]

    if 0 <= nr < N and 0 <= nc < M:
        print(arr[nr][nc], end = ' ')

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# r, c = 1, 1  # 기준점
# N, M = 3, 3
#
# # 4방향 델타 정의 (상, 하, 좌, 우)
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# for i in range(4):
#     nr = r + dr[i]  # next_row
#     nc = c + dc[i]  # next_column
#
#     # [핵심] 벽(경계) 체크: 이동 후 위치가 배열 범위를 벗어나지 않는지 확인
#     if 0 <= nr < N and 0 <= nc < M:
#         print(arr[nr][nc], end=' ')
