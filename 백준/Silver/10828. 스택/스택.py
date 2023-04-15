import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    commands = sys.stdin.readline().split()

    if commands[0] == "push":
        stack.append(commands[1])

    elif commands[0] == "pop":
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack.pop())
        
    elif commands[0] == "size":
        print(len(stack))

    elif commands[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        
    elif commands[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
