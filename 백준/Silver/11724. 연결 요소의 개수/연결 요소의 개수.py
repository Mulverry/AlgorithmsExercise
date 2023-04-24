import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
    
    
visited = [0]*(n)
ans = 0

def dfs(x):
    if visited[x] > 0:
        return
    visited[x] = 1
    for i in graph[x]:
        dfs(i)   
         
for i in range(n):
    if visited[i] == 0:
         ans += 1
         dfs(i)

print(ans)