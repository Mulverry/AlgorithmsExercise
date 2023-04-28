import sys

input = sys.stdin.readline

t = int(input())
count = 0

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())
    
    dp = [0 for _ in range(goal +1)]
    dp[0] = 1 # 0원을 만들 수 있는 경우는 무조건 1
    for c in coins:
        for i in range(c, goal+1): # ex) 2원동전은 2원부터 만들 수 있음
            dp[i] += dp[i-c]
            
    print(dp[goal])    