import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

q= deque([])

def bfs(row, col):
    q.append([row, col])
    graph[row][col] = 0 # 방문처리
    
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
        
            if 0<=nrow<n and 0<=ncol<m and graph[nrow][ncol] == 1:
                q.append([nrow, ncol])
                graph[nrow][ncol] = 0
                

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    worm = 0
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                worm += 1
                
    print(worm)