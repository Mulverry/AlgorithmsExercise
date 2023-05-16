#  https://peisea0830.tistory.com/3 참고


import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
height = 0
ans = sys.maxsize

for k in range(257):
    over = 0 # 현재 높이보다 높아야 하는 곳에 블록이 남는 경우
    below = 0 # 현재 높이보다 높아야 하는 곳에 블록이 부족한 경우
    for i in range(n):
        for j in range(m):
            if board[i][j] < k: 
                below += (k- board[i][j]) # 부족한 블록수
            else:
                over += (board[i][j]-k) #남는 블록수
    inven = over + b 
    if inven < below:
        continue
    time = 2*over + below #걸리는 시간
    if time <= ans:
        ans = time
        height = k
        
print(ans, height)