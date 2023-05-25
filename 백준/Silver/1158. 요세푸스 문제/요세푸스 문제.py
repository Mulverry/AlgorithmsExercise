import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ring = deque([i for i in range(1, n+1)])
yose = []


while ring:
    for j in range(k-1):
        ring.append(ring.popleft())
    yose.append(ring.popleft())
    
print(str(yose).replace('[', '<').replace(']', '>'))