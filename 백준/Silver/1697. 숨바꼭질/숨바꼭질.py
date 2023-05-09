import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0]*1000001           # n, k모두 0~100000까지 있음.
visited[n] = 1

q = deque([(n, 0)])
time = 0

def bfs():
    while q:
        pre, time = q.popleft()
        if pre == k:
            return time
        next = [pre+1, pre-1, pre*2]
        for i in next:
            if 0<=i<100001 and not visited[i]:
                visited[i] = 1
                q.append((i, time+1))

print(bfs())