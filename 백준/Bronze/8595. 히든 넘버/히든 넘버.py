import sys
input = sys.stdin.readline

n = input()
words = input()
hidden = ''
ans = 0

for i in words:
    if i.isdigit():
        hidden += i
    else:
        if hidden:
            ans += int(hidden)
            hidden = ''
if hidden:
    ans += int(hidden)

print(ans)