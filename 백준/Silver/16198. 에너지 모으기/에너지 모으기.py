# https://lemonjade.tistory.com/11

import sys
input = sys.stdin.readline

n = int(input())
balls = list(map(int, input().split()))
ans = 0

def dfs(balls, energy):
    global ans
    if len(balls) == 2: # 최대에너지 구하는 조건
        ans = max(energy, ans)
        return
            
    for i in range(1, len(balls)-1):
        new_balls = balls[:i] + balls[i+1:] # 선택한 구슬 제거
        dfs(new_balls, energy + (balls[i-1] * balls[i+1]))
        
dfs(balls, 0)

print(ans)