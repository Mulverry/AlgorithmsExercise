n, x = input().split()
n = int(n)
x = int(x)

a = list(map(int, input().split()))

new = []

for i in range(0, len(a)):
    if a[i] < x:
        new.append(a[i])    
    i += 1

print(*new, sep=" ")