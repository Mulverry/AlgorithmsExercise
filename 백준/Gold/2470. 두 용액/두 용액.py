import sys
input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))

liq.sort()

start = 0
end = len(liq) - 1
mix = sys.maxsize
ans = []

while start < end:
    new = liq[start] + liq[end]
    
    if abs(new) < mix:
        mix = abs(new)
        ans = [liq[start], liq[end]]
        
    if new > 0 :
        end -= 1
    
    elif new < 0 :
        start += 1
    
    else:
        break

print(*ans)
        