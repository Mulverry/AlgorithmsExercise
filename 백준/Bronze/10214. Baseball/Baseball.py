import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    sumy, sumk = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        sumy += y
        sumk += k

    if sumy > sumk:
        print("Yonsei")
    elif sumy < sumk:
        print("Korea")
    else:
        print("Draw")