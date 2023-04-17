import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    
    if x > 0:                       #heappush(추가할 리스트, 원소). 기본적으로 최소힙.
        hq.heappush(heap, (-x, x))  # 최대힙으로 바꾸려면 튜플 추가하여 (우선순위, 값)으로 변환.
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1]) #heappop(heap)만쓰면 튜플을 반환해버림
        else:
            print(0)