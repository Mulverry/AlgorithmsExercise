
from collections import deque
import sys

def turn(d, c): 
    if c == "L":
        d = (d-1) % 4 #왼쪽 꺾기: 상(0)- 좌(-1) -하(1) -우(1)-상(-1). direction-1인 이유는 board가 0으로 시작해서.
        return d
    else:
        d = (d+1) % 4 #오른쪽 꺾기: 상(0) - 우(1) - 하(1)- 좌(-1)-상(-1)
        return d

drow = [-1, 0, 1, 0] # (0,0)좌표에서 움직일 때: 하-우-상-좌 #참조:N-queens.  # x,y로 생각하기보다 row, col로 생각해야 함.
dcol = [0, 1, 0, -1]


def start():
    direction = 1 #초기방향
    time = 1 # 시간
    row, col = 0, 0 # 초기 뱀 위치
    visited = deque() # 방문위치
    visited.append([row, col])
    board[row][col] = 2         # 뱀이 이동했으면 2로 표시
    
    while True:
        row = row + drow[direction]
        col = col + dcol[direction]

        if 0 <= row < n and 0 <= col < n and board[row][col] !=2 :
            if not board[row][col] == 1: # 사과가 없는 경우. board[row][col]가 1인 경우가 아니면
                tmp_row, tmp_col = visited.popleft()
                board[tmp_row][tmp_col] = 0 # 꼬리 제거
             
            board[row][col] = 2 # 위의 사과가 없는 경우랑 상관없이 뱀이 이동함. 위에 else문 쓰면 안 됨.
            visited.append([row, col]) # 뱀 머리를 큐에 넣음
            
            if time in times.keys():
                direction = turn(direction, times[time])
            
            time += 1 #어떤 경우에라도 시간은 감.

        else: # 자기 몸에부딪히거나, 벽에 부딪힌 경우
            return time
                


input = sys.stdin.readline
n = int(input()) # 보드판
board = [[0]*n for _ in range(n)]

k = int(input()) #사과
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1 # 사과가 있으면 1로 표시
    

l = int(input()) # 뱀의 방향 변환
times = {} # 딕셔너리

for _ in range(l):
    x, c = input().split() # 정수, 문자열의 경우에는 map 쓸 필요 없이 sys.stdin.readline().split() 쓰면 됨
    times[int(x)] = c # times = {3: d, 15:l, 17:d} 이렇게 넣겠다는 소리
    
print(start())