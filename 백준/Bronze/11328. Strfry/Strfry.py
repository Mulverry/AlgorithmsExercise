import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    word = input().split()
    left = list(word[0])
    right = list(word[1])
    if sorted(left) == sorted(right):
        print("Possible")
    else:
        print("Impossible")