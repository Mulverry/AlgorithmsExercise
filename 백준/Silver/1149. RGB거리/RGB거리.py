# https://cotak.tistory.com/11

import sys
input = sys.stdin.readline

n = int(input())
r, g, b = 0, 1, 2
costs = [list(map(int, input().split())) for _ in range(n)] #1번집 : r, g, b / 2번집: r,g,b...

dp = [[0]*3 for _ in range(n)]
dp[0][r], dp[0][g], dp[0][b] = costs[0][r], costs[0][g], costs[0][b]

for i in range(1, n):
    dp[i][r] = min(dp[i-1][g], dp[i-1][b]) + costs[i][r] #이전 선택한 값 중 최소 + 현재값
    dp[i][g] = min(dp[i-1][r], dp[i-1][b]) + costs[i][g]
    dp[i][b] = min(dp[i-1][r], dp[i-1][g]) + costs[i][b]
    
print(min(dp[n-1]))