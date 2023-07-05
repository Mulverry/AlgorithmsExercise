n = int(input())

for i in range(1, n+1):
    part = list(map(int, str(i)))
    m = i + sum(part)
    if m == n:
        print(i)
        break
    if i == n:
        print(0)