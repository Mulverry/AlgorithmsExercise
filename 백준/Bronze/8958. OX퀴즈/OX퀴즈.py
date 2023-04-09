n = int(input())

for i in range(n):
    oxList = list(input()) # list입력을 n번 반복
    score = 0
    total = 0
    
    for j in oxList:
        if j == "O":
            score += 1
            total += score 
        else:
            score = 0
    
    print(total)
    