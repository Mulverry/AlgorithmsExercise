import sys, heapq
from heapq import heappush, heappop, heapify

input = sys.stdin.readline
v, e = map(int, input().split())

# 그래프 구성
graph = [[] for _ in range(v+1)] # v가 아니라 v+1을 넣은 이유: A가 graph[1]부터 시작해야 노드 식별이 쉬워서.
for _ in range(e):
    now, next, weight = map(int, input().split())
    graph[now].append([weight, now, next])
    graph[next].append([weight, next, now])


# Prim
hq, distance, cnt = [], 0, 0 # 초기값 설정
visited = [False]*(v+1)

# 시작노드를 임의로 1로 정함. 노드를 방문체크. 시작노드 1과 연결된 모든 간선을 힙에 넣음.
start = graph[1]
visited[1] = True
total_weight = 0
for i in graph[1]:
    heapq.heappush(hq, i) # 기본적으로 최소힙

# pq에서 가장 cost가 낮은 간선 heappop(루트노드 갈아끼우기)
while hq:
    weight, now, next = heapq.heappop(hq)
    if visited[next] == False: # 다음 노드를 방문하지 않았다면
        visited[next] = True
        total_weight += weight
        
        for edge in graph[next]:
            if visited[edge[2]] == False:
                heappush(hq, edge)

print(total_weight)