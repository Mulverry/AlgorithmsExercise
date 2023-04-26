# BFS
# 

import sys, heapq
from collections import deque
sys.setrecursionlimit = 10**6

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(row, col):
    visited = [[False]*n for _ in range(n)]
    q = [] #우선순위큐: 최소의 수 구하므로
    heapq.heappush(q, (0, row, col))
    
    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]
    
    while q:
        cnt, row, col = heapq.heappop(q)
        
        if row == n-1 and col == n-1:
            return cnt 
    
        for i in range(4): # 방향전환
            nrow = row + drow[i]
            ncol = col + dcol[i]
    
            if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                if graph[nrow][ncol] == 0: # 최소 경로에 0이 있으면 cnt +1
                    heapq.heappush(q, (cnt+1, nrow, ncol))
                else:
                    graph[nrow][ncol] = 1
                    heapq.heappush(q, (cnt, nrow, ncol))
                
print(bfs(0, 0))