import sys
from collections import deque

n = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))

stack = deque([])
ans = [0]*n

for i in range(n): # 오답이유: 스택에 2개 저장될 수 있는지 몰랐음.
    while stack:
        if stack[-1][1] > tower[i]: #스택의 가장 윗부분[-1,stack[-1]]에서 stack[-1](높이)이 i번째 타워보다 크다면
            ans[i] = stack[-1][0] + 1 # 스택의 가장 윗값의 인덱스 + 1을 답에 저장. 탑의 번호는 1부터 시작하므로.
            break
        else:
            stack.pop()
    stack.append([i, tower[i]]) # 저장할 때부터 인덱스와 값을 둘 다 저장. [인덱스, 값] stack: [[0, tower[0]], [1, stack[1]], ....]
    
print(*ans)