import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
a = '0' + input().rstrip()  # rstrip 안 하면 \n이 남아버림. 앞에 0붙인 이유는 a[i]가 i번째임을 바로 알기 위해서

graph = [[] for _ in range(n+1)] 
for _ in range(1, n):
    x, y = map(int, input().split())
    graph[x].append(y) # 양방향. 4에 시작해서 1에 끝날 수도 있음.
    graph[y].append(x)

visited = [False]*(n+1)
cnt = 0

def dfs(start):
    global cnt
    for i in graph[start]: # start 노드와 인접한 노드들 중에서
        if visited[i] == False:
            if a[i] == "1":
                cnt += 1
                visited[i] = True
                dfs(i)
            else:
                visited[i] = True
                dfs(i)
                
                  
for i in range(1, n+1):
    dfs(i)

print(cnt)