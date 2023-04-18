import sys
import heapq

input = sys.stdin.readline

n = int(input())
Lheap = [] # 중간값보다 작은 수. 하지만 그동안 외친 수가 짝수개라면 두 수 중에서 작은 수를 말해야 하기에 중간값은 Lheap에 있어야 함
Rheap = [] # 중간값보다 큰 수

for _ in range(n):
    num = int(input())
    
    if len(Lheap) == len(Rheap): 
        heapq.heappush(Lheap, (-num)) # Lheap은 최대힙.Rheap이 최소힙일때, Lheap의 첫 원소는 중간값. Rheap(최소->최대) /\ Lheap(최대->최소)
    else: # 그동안 외친 수의 개수가 홀수개라면 
        heapq.heappush(Rheap, (num)) # Rheap은 최소힙.
        
    if Rheap and (Rheap[0] < -Lheap[0]): #Rheap에 원소를 넣는 차례에, Rheap의 첫원소가 Lheap보다 작다면 Rheap은 중간값보다 커야 한다는 조건을 위배함
        Lvalue = heapq.heappop(Lheap)
        Rvalue = heapq.heappop(Rheap) # 내용물 바꿈
        
        heapq.heappush(Lheap, -Rvalue)
        heapq.heappush(Rheap, -Lvalue)
    
    print(-Lheap[0]) # 중간값은 Lheap의 첫 원소. Lheap에 heappush할 때 -num했으므로 출력할 때는 - 해제