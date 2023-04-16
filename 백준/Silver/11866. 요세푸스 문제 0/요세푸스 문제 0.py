import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

ring = deque([i for i in range(1, n+1)])
yose = []

while ring:
    for j in range(k-1):
        num = ring.popleft()
        ring.append(num)
    num = ring.popleft()
    yose.append(num)

print("<", end="")
print(', '.join(map(str, yose)), end = "")
print(">")