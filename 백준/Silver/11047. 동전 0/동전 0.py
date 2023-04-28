import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

num_list = []
for i in coins:
    num_list.append(k//i)
    k = k % i
    
print(sum(num_list))