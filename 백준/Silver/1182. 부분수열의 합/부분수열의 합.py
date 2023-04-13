
from itertools import combinations

n, s = map(int, input().split())
ans = 0

arr = list(map(int, input().split())) #시간 초과: list를 아직도 잘 못 씀
    
for i in range(1, len(arr)+1):
    part = list(combinations(arr, i))
    for j in part: # 오답: for j를 넣지 않자 조합의 원소가 아니라 조합 그 자체가 선택되어버림.
        if sum(j) == s:
            ans += 1

print(ans)