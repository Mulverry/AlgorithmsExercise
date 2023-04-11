# Bruteforce, 정렬
# https://jitolit.tistory.com/122

import sys

hobbits = []

for _ in range(9):
    h = int(sys.stdin.readline().strip())
    hobbits.append(h)

hobbits.sort()

sum = sum(hobbits)

# 9명 중 사기꾼 2명 난쟁이를 찾는데, 전체 합 - 사기꾼 합 = 100

for i in range(len(hobbits)):
    for j in range(len(hobbits)):
        if sum - (hobbits[i]+hobbits[j]) == 100:
            fake = {hobbits[i], hobbits[j]}

result = [_ for _ in hobbits if _ not in fake]

print(*result, sep="\n")