import sys

n = int(sys.stdin.readline()) # 도시 개수
travel_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0]*n
ans = sys.maxsize # sys.maxsize = 파이썬에서 표기할 수 있는 최댓값

def dfs(start, now, cost, visited): #시작도시, 현재도시, 비용, 방문도시
    global ans
    
    if len(visited) == n: # 방문완료된 도시가 입력받은 도시의 개수와 같다면(도시를 전부 방문)
        if travel_cost[now][start] != 0: # 마지막 도시에서 출발 도시로 갈 수 있다면
            cost += travel_cost[now][start]
            ans = min(ans, cost)
        return 

    for i in range(n): # 도시의 개수만큼 반복문을 도는데
        # 현재 도시에서 다음 도시로 갈 수 있고, 그 도시가 이미 방문한 도시가 아니며, 비용이 저장되어 있는 최소값보다 작다면
        if travel_cost[now][i] !=0 and (i not in visited) and cost < ans:
            visited.append(i)
            dfs(start, i, cost+travel_cost[now][i], visited) # 그 도시를 방문함
            visited.pop() # 방문을 완료했다면 방문목록 해제

# 도시(0~3)마다 출발점 지정
for i in range(n):
    dfs(i, i, 0, [i])

print(ans)