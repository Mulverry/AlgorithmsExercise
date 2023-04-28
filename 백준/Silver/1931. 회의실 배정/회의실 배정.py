import sys
input = sys.stdin.readline

n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]

meeting.sort(key=lambda x: (x[1], x[0])) # 빨리 끝나는 순서대로 정렬. 끝나는 시간이 같으면 시작기준으로 정렬.

now = 0
count = 0 #회의실 사용가능한 회의 개수
for i in meeting:
    if now <= i[0]: # 현재시각이 회의 시작시간보다 작거나 같으면
        count += 1
        now = i[1] # 현재시각을 회의 끝나는 시각으로 변경

print(count)