import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    data = pow(a, b, 10)
    if data == 0:
        print(10)
    else:
        print(data)