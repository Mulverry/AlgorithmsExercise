import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    h = int(sys.stdin.readline())
    stack.append(h)

side = stack[-1] # 옆에서 보는 막대기의 최소 높이
ans = 1 # 옆에서 적어도 막대기 하나는 보고 있으므로

for i in reversed(stack): # reversed 안쓰면 처음부터 높은 막대가 나와버렸을 때 side가 갱신되어 다음으로 진행을 못 한다. 
    if i > side:
        side = i
        ans += 1
    else:
        pass

print(ans)