import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
cur = 1
temp = True

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        cur += 1
        ans.append("+")
        
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        temp = False
        break
        
if temp == False:
    print("NO")
else:
    for i in ans:
        print(i)