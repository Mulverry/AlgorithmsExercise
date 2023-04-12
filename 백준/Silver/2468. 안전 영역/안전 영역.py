import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
boards = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 십자가 모양 최소단위 표기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 침수 여부 확인할 수 있는 Boolean Table 생성. False n칸 * n줄
done = [[False]*n for _ in range(n)]

# x, y 기준으로 주변 탐색하는 재귀 함수. h는 강수량.
def dfs(x, y, h):
    # x,y 좌표를 기준으로 상하좌우 좌표를 new_x 포문으로 가져옴. 상하좌우므로 4.
    for m in range(4):
        new_x = x + dx[m]
        new_y = y + dy[m]
                
        # 자신이 건너갈 new_x, new_y 좌표에 대한 유효성promising을 검증
        # new_x, new_y좌표가 보드판 위에 있어야 하고, 물높이보다 위에 있어야 함.
        if (0 <= new_x < n) and (0 <= new_y < n) and boards[new_x][new_y] > h and not done[new_x][new_y]:
            #유효성이 검증된 좌표에 한해서 재귀함수를 호출. 
            done[new_x][new_y] = True
            # 실질적으로 dfs 재귀함수가 하는 역할은 sunk_boards에 boolean값만 바꾸는 역할
            dfs(new_x, new_y, h)

ans = 1 # 안전영역이 적어도 하나는 나올 것이므로.


for k in range(max(map(max, boards))): # boards의 각 행의 max값이 들어간 리스트를 또 max
    count = 0
    done = [[False]*n for _ in range(n)] # 오답이유 : visited 초기화 해야 함.
    for i in range(n):
        for j in range(n):
            if boards[i][j] > k and done[i][j] == False:
                done[i][j] = True
                count += 1
                dfs(i, j, k)
    
    ans = max(ans, count)

print(ans)