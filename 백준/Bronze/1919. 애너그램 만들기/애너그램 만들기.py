a = [0]*26
b = [0]*26
ans = 0

first = input()
second = input()

for i in first:
    a[ord(i)-97] += 1
for i in second:
    b[ord(i)-97] += 1

for i in range(26):
    ans += abs(a[i] - b[i])

print(ans)
