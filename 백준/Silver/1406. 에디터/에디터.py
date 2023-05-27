import sys

left = list(input())
right = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and left:
        right.append(left.pop())
    elif command[0] == "D" and right:
        left.append(right.pop())
    elif command[0] == "B" and left:
        left.pop()
    elif command[0] == "P":
        left.append(command[1])

print("".join(left + list(reversed(right))))