# https://velog.io/@chez_bono/%EB%B0%B1%EC%A4%80-5397-%ED%82%A4%EB%A1%9C%EA%B1%B0


import sys
input = sys.stdin.readline
l = int(input())

for i in range(l):
    word = list(input().strip())
    left = []
    right = []
    for p in word:
        if p == "<":
            if left:
                right.append(left.pop())
        elif p == ">":
            if right:
                left.append(right.pop())
        elif p == "-":
            if left:
                left.pop()
        else:
            left.append(p)
    left.extend(reversed(right))
    print(*left, sep="")