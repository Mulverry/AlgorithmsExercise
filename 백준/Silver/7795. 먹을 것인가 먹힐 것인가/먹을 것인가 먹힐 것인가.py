import sys
input = sys.stdin.readline

def binary_s(listb, target):
    start = 0
    end = len(listb)-1
    
    while start <= end:
        mid = (start + end) // 2
        if target > listb[mid]:
            start = mid + 1
        else:
            end = mid-1
    
    return start #target이 클 경우만 생각하므로.

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    ans = 0
    
    for i in a:
        cnt = binary_s(b, i)
        ans += cnt

    print(ans)
