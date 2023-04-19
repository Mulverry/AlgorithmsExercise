import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = [0]*n  

for i in range(len(a)):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))