import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for i in range(1, n):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(root):
    for i in tree[root]:
        if parent[i] == 0:
            parent[i] = root
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])