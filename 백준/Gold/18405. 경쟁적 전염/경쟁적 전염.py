import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

def bfs():
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 :
                virus.append((graph[i][j], i, j, 0)) # 바이러스종류, 좌표, 탐색시간 초깃값 넣어줌
    
    virus.sort(key=lambda x:x[0])  # 0번째인 graph[i][j] 기준으로 정렬
    q= deque(virus)
    
    while q:
        name, row, col, time = q.popleft()
        if time == s:
            break
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            
            if 0 <=nrow < n and 0<=ncol <n and graph[nrow][ncol] == 0:
                graph[nrow][ncol] = name
                q.append((graph[nrow][ncol], nrow, ncol, time+1))
        
bfs()

print(graph[x-1][y-1])
                
        
        