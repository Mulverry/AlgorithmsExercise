# permutation 순열 사용

from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

cases = list(permutations(a))
answer = 0         # answer에 0을 넣는 이유: 최댓값을 구하려면 비교를 해야 하니까.

for case in cases:
    sum = 0
    for i in range(n-1):
        sum += abs(case[i] - case[i+1])
    answer = max(answer, sum)
    
print(answer)