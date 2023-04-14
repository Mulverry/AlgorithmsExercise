import sys

n = int(sys.stdin.readline())
match = list(map(int, sys.stdin.readline().split())) # n개

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split())) # arr은 m개 수 들어있는 리스트
result = [0] * m

match.sort()

# 이분탐색 사용

for i in range(m): # arr의 원소가 match의 어디에 있는지 매치
    start = 0
    end = len(match) -1
    
    while start <= end:
        mid = (start+ end) // 2
        
        if arr[i] == match[mid]:
            result[i] = 1
            break
        elif arr[i] < match[mid]: # arr의 원소가 match의 왼쪽에 있다면
            end = mid-1
        else: # arr의 원소가 match의 오른쪽에 있다면
            start = mid+1

print(*result, sep="\n")