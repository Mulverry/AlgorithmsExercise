# DFS , 백트래킹

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # + - * //

max_val = -1e9
min_val = 1e9

def dfs(depth, data, add, sub, mul, div):
    global max_val, min_val
    
    if depth == n:
        max_val = max(max_val, data)
        min_val = min(min_val, data)
        return
    
    if add: # 연산자가 있으면 아래. 없으면 안감(백트래킹)
        dfs(depth+1, data + nums[depth], add - 1, sub, mul, div)
    if sub:
        dfs(depth+1, data - nums[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, data * nums[depth], add, sub, mul-1, div)
    if div:
        if data > 0:
            dfs(depth+1, data // nums[depth], add, sub, mul, div-1)
        else:
            dfs(depth+1, -(-data // nums[depth]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)

print(max_val)
print(min_val)