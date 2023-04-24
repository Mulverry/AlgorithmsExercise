import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
in_degree = [0]*(n+1)
queue = deque([])
ans = []

for _ in range(m):
    a, b = list(map(int, input().split()))
    in_degree[b] += 1 # a- > b로 갈 때 b도시 입장에서는 진입차수 1씩 증가
    graph[a].append(b)
    
for i in range(1, n+1):
    if in_degree[i] == 0: #진입차수가 0이면 해당학생번호를 큐에 넣음
        queue.append(i)
        
while queue:
    now = queue.popleft()
    ans.append(now)
    
    for i in graph[now]:
        in_degree[i] -= 1 # 진입차수의 개수를 1 감소
        if in_degree[i] == 0: # 만약 진입차수가 0이 되면 큐에 넣음
            queue.append(i)
     
print(*ans, end = " ")
