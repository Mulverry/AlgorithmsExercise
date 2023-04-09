def han(num) :
    cnt = 0
    for i in range(1, num+1):
        line = list(map(int,str(i)))
        if i < 100:
            cnt += 1  # 100보다 작으면 모두 한수
        elif line[0]-line[1] == line[1]-line[2]:
            cnt += 1  # x의 각 자리가 등차수열이면 한수
    return cnt

num = int(input())
print(han(num))