# 조합 사용
from itertools import combinations
import sys

hobbits = [int(input()) for _ in range(9)]
occation = list(combinations(hobbits, 7))

for i in occation:
    if sum(i) == 100:
        answer = sorted(list(i))

print(*answer, sep = "\n")
