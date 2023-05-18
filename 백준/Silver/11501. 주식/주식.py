#https://kkk4872.tistory.com/139

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    days = list(map(int, input().split()))
    value = 0
    max = 0
    
    for i in range(len(days)-1, -1, -1):
        if (days[i] > max):
            max = days[i]
        else:
            value += max-days[i]
    
    print(value)