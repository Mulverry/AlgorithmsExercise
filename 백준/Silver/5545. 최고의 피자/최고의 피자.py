
import sys
input = sys.stdin.readline

n = int(input())
dough, topping = map(int, input().split())
doughC = int(input())
toppingC = [int(input()) for _ in range(n)]

toppingC.sort(reverse=True) #토핑의 칼로리를 내림차순으로 정렬

nowP = dough
nowC = doughC
ans = doughC/dough # 토핑 안 얹고 도우만 시켰을 때

#토핑의 열량을 높은 것 부터 차례로 넣어보면서 1원당 칼로리 계산
#이전 칼로리보다 높으면 정답 변경

for i in toppingC:
    tempC = nowC + i
    tempP = nowP + topping
    
    if tempC/tempP > ans:
        ans = tempC/tempP
        nowC = tempC
        nowP = tempP
    else:
        break
    
print(int(ans))
    