# https://wooono.tistory.com/628
# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     stick, ants = map(int, input().split())
#     ant_places = [int(input()) for _ in range(ants)]
#     fall = []
#     for i in range(len(ant_places)):
#        fall.append(stick-ant_places[i])
#     fast, slow = min(fall), max(fall)
#     print(fast, slow)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    stick, num = map(int, input().split())
    ants = [int(input()) for _ in range(num)]
    
    min_time = []
    max_time = []
    
    for ant in ants:
       min_time.append(min(ant,stick-ant))
       max_time.append(max(ant, stick-ant))
    print(max(min_time), max(max_time)) # 개미가 '모두' 땅으로 떨어지는 시간을 구한다. 가장 먼저 떨어지는 개미가 아님.
    