import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [(0, 0)]
for _ in range(n):
    items.append(tuple(map(int, input().split())))
    
dp = [[0]*(k+1) for _ in range(n+1)]

# dp 배열 채우기
for i in range(1, n+1): # i는 물건 종류
    w, v = items[i]
    for j in range(1, k+1): # k는 배낭 무게
        if w <= j: # 현재 물건을 선택한다면
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j]) # 예전 물건(=[i-1])의 [j-w](=가방의 남은 무게) + 현재 물건의 가치
        else:
            dp[i][j] = dp[i-1][j] # 현재 물건을 선택하지 않는 경우 이전 물건으로 k를 채우려고 함
            
print(dp[n][k])