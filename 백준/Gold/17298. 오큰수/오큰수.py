import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = [] # 오큰수 찾지 못한 인덱스 저장. 
ans = [-1]*n

for i in range(len(arr)):
    while stack and (arr[stack[-1]] < arr[i]): # 현재 수열의 수가 스택의 가장 위에 있는 인덱스의 수보다 크다면
        ans[stack.pop()] = arr[i]
    stack.append(i) # 0, 1, 2, 3..
print(*ans)