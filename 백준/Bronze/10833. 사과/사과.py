import sys
input = sys.stdin.readline

school = int(input())
ans = 0

for _ in range(school):
    student, apple = map(int, input().split())
    left = apple % student
    ans += left

print(ans)