import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

occasion = list(combinations(cards, 3))
ans = []

for i in occasion:
    if sum(i) <= m:
        ans.append(sum(i))
    else:
        continue

print(max(ans))    