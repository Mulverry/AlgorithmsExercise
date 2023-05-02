import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]
count = []

def bfs(row, col):
    cnt = 1
    q= deque([(row, col)])
    
    while q: #while q를 자꾸 까먹는다..
        row, col = q.popleft()
        visited[row][col] = 1 # visited를 어디다가 넣는지가 관건
        
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0<=nrow<n and 0<=ncol<n and not visited[nrow][ncol] and graph[nrow][ncol] == 1:
                cnt += 1
                graph[nrow][ncol] += 1
                q.append((nrow, ncol))
                
    count.append(cnt)
            
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1:
            bfs(i, j)

count.sort()
print(len(count), *count, sep="\n")