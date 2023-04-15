import sys

t = int(sys.stdin.readline().strip())


for _ in range(t):
    strings = input() # sys.stdin.readline().split()으로 쓰니 안 돌아간다.
    stack = []
    
    for i in strings:
        if i == "(" :
            stack.append(i)
        elif i == ")":
            if len(stack) != 0: 
                stack.pop()
            else:
                print("NO")
                break
    
    else :  # for-else문. break문으로 끊기지 않고 수행됐을 경우
        if not stack: # break문으로 끊기지 않고 스택이 비어있다면 괄호 다 맞음 / not은 비어있음
            print("YES")
        else:
            print("NO") # 스택 안에 괄호가 남아있으면 no
