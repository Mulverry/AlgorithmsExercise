# 큐

import sys
from collections import deque 

n = int(sys.stdin.readline())
queue = deque([]) #deque 안 하니까 시간초과 발생


for _ in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(order[1])
    
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft()) # deque해야 popleft 사용가능
    
    elif order[0] == 'size':
        print(len(queue))
    
    elif order[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    
    elif order[0] == 'front':
        if len(queue) == 0 :
            print(-1)
        else:
            print(queue[0])
    
    elif order[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])