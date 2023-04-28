
import sys
input = sys.stdin.readline

t = int(input())
apply = []

for _ in range(t):
    n = int(input())
    rank = [tuple(map(int, input().split())) for _ in range(n)]
    rank.sort() # 서류 성적 순으로 정렬. 이제 면접 순위만 비교하면 됨.
    apply.append(rank)
    
    criteria = rank[0][1] # 기준 = 류순위 1등의 면접순위 (1,4)의 4
    hired =1 # 서류순위 1등은 이미 합격이므로.
    
    for i in range(1, n):
        if rank[i][1] < criteria: # 기준보다 순위가 높다면
            criteria = rank[i][1]
            hired += 1
    
    print(hired)    
