import sys

n = int(sys.stdin.readline())

# 0이 10001(=n의 최댓값+1. 0~10000)개 들어간 a라는 리스트를 만듦. 
a = [0] * 10001 

# 숫자를 입력받고, a의 숫자번째 자리에 1이 들어가게 함.
for i in range(n):
    num = int(sys.stdin.readline())
    a[num] += 1 

# a를 다 훑어서 a의 숫자번째 자리가 1넘으면(중복값 포함), 그 수만큼 인덱스 출력
for i in range(1, 10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)