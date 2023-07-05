import sys
input = sys.stdin.readline

words = list(input().strip())
bomb = list(input().strip())
stack = []

for i in range(len(words)):
    stack.append(words[i])
    if stack[-len(bomb):] == bomb:
        for i in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")