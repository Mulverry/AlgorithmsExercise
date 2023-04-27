import sys
input = sys.stdin.readline

n = int(input())

# 1. 테이블 정의하기: fibo[i] = i번째 오는 피보나치 수열
# 2. 점화식 찾기: fibo[n] = fibo[n-1] + fibo[n-2]
# 3. 초기값 정하기 -> 반복문으로 배열 채우기

fibo = [0]*(n+1) # 밑에 반복문 range가 n+1이므로
fibo[0] = 0
fibo[1] = 1

for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])
