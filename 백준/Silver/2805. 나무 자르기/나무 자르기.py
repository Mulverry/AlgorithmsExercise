# 이분탐색

import sys

n, m = map(int, sys.stdin.readline().split())
trees = sorted(list(map(int, sys.stdin.readline().split())))
   
start = 1
end = max(trees)

# start와 end가 같아질 때까지 자르는 걸 반복
while start <= end:
    mid = (start + end) //2
    cut = mid
    savings = 0
    
    for tree in trees: # 오답이유 : 최종 savings과 mid 사이의 상관관계를 인식 못했음
        if tree > cut:
            savings += tree - cut  
    if savings < m: # 목표보다 덜 잘랐으므로 기준 낮춰서 자를 필요 있음
        end = mid - 1        
    else: # 목표보다 더 잘랐으므로 기준 높여서 잘라야 함
        start = mid + 1

print(end)