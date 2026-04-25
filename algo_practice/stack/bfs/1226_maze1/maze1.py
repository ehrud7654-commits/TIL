import sys
sys.stdin = open('input.txt')

from collections import deque

T = 10

for _ in range(T):

    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    start_x, start_y = 0, 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    visited = [[False]*16 for _ in range(16)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y] = True

    answer = 0

    while queue:
        x, y = queue.popleft()

        if maze[x][y] == 3: #도경아 이거 == 이잖아
            answer = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 16 and 0 <=ny < 16:
                if not visited[nx][ny] and maze[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

    print(f'#{tc} {answer}') # 이거는 tab하나 해야지 도경아. 애초에 그리고 지금 result 변수가 없잖아. answer로 해놨잖아
    #tu es stupido