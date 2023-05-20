import sys
input = sys.stdin.readline

n = int(input()) #거리 길이
m = int(input()) #가로등 개수
lights = list(map(int, input().split())) #가로등 위치
max_cover = 0

for i in range(1, len(lights)):
    max_cover = max(max_cover, lights[i]-lights[i-1])
    
print(max((max_cover+1)//2, lights[0]-0, n - lights[-1])) # 두 가로등 사이의 거리니까 가로등이 둘 다 켜져서 비춰주는 경우의 높이 구해야함.