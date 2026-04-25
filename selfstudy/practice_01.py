import sys
sys.stdin = open('input.txt')

from collections import deque

T = 10

for _ in range(T):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]


    start_x , start_y = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 3:
                start_x, start_y = i, j

    visited = [[False] * 16 for _ in range(16)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((start_x))


