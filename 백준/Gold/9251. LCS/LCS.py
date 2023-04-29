import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
cache = [0] * (len(b))

for i in range(len(a)):
    cnt = 0
    for j in range(len(b)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif a[i] == b[j]:
            cache[j] = cnt + 1
            
print(max(cache))       