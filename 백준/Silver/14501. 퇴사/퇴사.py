import sys
input = sys.stdin.readline

n = int(input())
consult = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def dfs(day, total):
    global ans

    if day == n:
        ans = max(ans, total)
        return
    
    time = consult[day][0]
    pay = consult[day][1]
    
    #해당일부터 상담하는 경우
    if day + time <= n: # 오답이유 : day + time <= n이라는 개념을 떠올리지 못함.
        dfs(day + time, total + pay)
    #해당일 다음날부터 상담하는 경우
    dfs(day +1, total)

for day in range(n):
    dfs(day, 0)
print(ans) 