import sys
input = sys.stdin.readline

n = int(input())
e = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
cnt = 0 

def dfs(x):
    global cnt
    if visited[x] == True:
        return x
    else:
        visited[x] = True
        cnt += 1
        for i in graph[x]:
            dfs(i)

dfs(1)
print(cnt-1)