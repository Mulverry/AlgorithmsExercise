from collections import deque
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
 
dx = [-1,1,0,0]
dy = [0,0,1,-1]
 
def bfs(a,b):
    queue = deque([[a,b]])
    while(queue):
        x,y = queue.popleft()
 
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<n and 0<=yy<m and graph[xx][yy]==1:
                queue.append([xx,yy])
                graph[xx][yy] = graph[x][y]+1
bfs(0,0)           
print(graph[n-1][m-1])    