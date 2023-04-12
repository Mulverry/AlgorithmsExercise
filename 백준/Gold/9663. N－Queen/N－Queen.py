import sys
n = int(sys.stdin.readline())
cnt = 0
row = [0] * n

def promising(x):
    for i in range(x):
        # 같은 행에 있거나 대각선에 있는 경우
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(i - x):
            return False
    return True

def queens(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            row[x] = i
            if promising(x):
                queens(x+1)

queens(0)
print(cnt)