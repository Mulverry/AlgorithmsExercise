# https://pacific-ocean.tistory.com/297
# https://unie2.tistory.com/1332

import sys, heapq
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
ans = 0
q = deque([])

# 그래프 만들기
graph = []
for z in range(h):
    floor = []
    for x in range(n):
        floor.append(list(map(int, input().split())))
        for y in range(m):
            if floor[x][y] == 1: # 익은 토마토라면 큐에 저장 
                q.append([z, x, y])
    graph.append(floor)

dhei = [0, 0, 0, 0, 1, -1]
drow = [1, -1, 0, 0, 0, 0]
dcol = [0, 0, 1, -1, 0, 0]

def bfs():
    while q:
        hei, row, col = q.popleft()
        
        for i in range(6):
            nhei = hei + dhei[i]
            nrow = row + drow[i]
            ncol = col + dcol[i]
            
            if 0 <= nhei < h and 0 <= nrow < n and 0 <= ncol < m and graph[nhei][nrow][ncol] == 0: # 범위 내에서 새로운 좌표가 0이라면 1로 바꿈
                graph[nhei][nrow][ncol] = graph[hei][row][col] + 1
                q.append([nhei, nrow, ncol])

bfs()

for z in range(h):
    for x in range(n):
        for y in range(m): 
            if graph[z][x][y] == 0: #bfs 종료 후 안 익은 토마토가 하나라도 발견된다면
                print(-1)
                sys.exit()
        ans = max(ans, max(graph[z][x])) 

print(ans -1)