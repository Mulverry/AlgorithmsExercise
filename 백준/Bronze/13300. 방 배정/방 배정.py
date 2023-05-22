import sys
input = sys.stdin.readline

n, k = map(int, input().split())
female = [0]*7
male = [0]*7

room = 0

for i in range(n):
    sex, year = map(int, input().split())
    if sex == 0:
        female[year] += 1
    else:
        male[year] += 1

for i in range(1, 7):
    if female[i] % k == 0 :
        room += (female[i]//k)
    else:
        room += (female[i]//k) + 1

    if male[i] % k == 0:
        room += (male[i]//k)
    else:
        room += (male[i]//k) + 1
        
print(room)