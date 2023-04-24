import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
edges = [list(map(int, input().split())) for _ in range(m)]

for e in edges:
    graph[e[0]].append(e[1])

distance = [-1]*(n+1)
visited = [False]*(n+1)

def bfs(k):
    queue = deque([x])
    visited[x] = True
    distance[x] = 0
    ans = []
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    ans.append(i)
    
    if len(ans) == 0:
        print(-1)
    else:
        print(*sorted(ans))

bfs(k)