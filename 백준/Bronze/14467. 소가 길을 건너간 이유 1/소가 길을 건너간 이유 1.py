#  https://imzzan.tistory.com/94

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
cow = [-1]*11

for _ in range(n):
    num, loca = map(int, input().split())
    if cow[num] == -1:
        cow[num] = loca
    elif cow[num] != loca:
        cow[num] = loca
        cnt += 1

print(cnt)