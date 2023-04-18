import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = sorted([int(input()) for _ in range(n)])

ans = 0

for i in range(len(cards)-1):
    a = heapq.heappop(cards) # 가장 작은 아이템을 pop
    b = heapq.heappop(cards)
    c = a + b
        
    ans += c
    heapq.heappush(cards, c)
        
print(ans)
