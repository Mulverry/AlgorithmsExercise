# 다익스트라 알고리즘
# https://blog.encrypted.gg/1037

import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, fare = map(int, input().split())
    graph[a].append([fare, b])

start, end = map(int, input().split())
min_cost = [int(1e9)]*(n+1) # 최소비용 테이블

def dijkstra(start):
    q = [] # 우선순위큐 사용: 항상 비용이 작은 것부터. 미니힙.
    heapq.heappush(q, (0, start)) # 출발도시의 비용과 노드를 힙에 저장
    min_cost[start] = 0
    
    while q:
        cost, now = heapq.heappop(q) # cost, now = fare, b
    
        if min_cost[now] < cost:
            continue # 왜?
            # min_cost[now] = cost
            
        for new_fare, new_start in graph[now]:
            new_cost = cost + new_fare
            
            if min_cost[new_start] > new_cost:
                heapq.heappush(q, (new_cost, new_start))
                min_cost[new_start] = new_cost

dijkstra(start)

print(min_cost[end])