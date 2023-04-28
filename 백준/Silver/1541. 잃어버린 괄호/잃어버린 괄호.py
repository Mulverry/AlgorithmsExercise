import sys
input = sys.stdin.readline

ans = 0

line = input().split("-") # split 기준으로 나눠서, line[0]과 -line[나머지]로 나뉨. 

for i in line[0].split("+"):
    ans += int(i)

for i in line[1:]:
    for j in i.split("+"):
        ans -= int(j)
        
print(ans)