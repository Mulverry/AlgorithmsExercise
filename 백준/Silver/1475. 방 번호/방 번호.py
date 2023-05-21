word = input()
set = [0]*10

for i in range(len(word)):
    num = int(word[i])
    set[num] += 1

set[6] = (set[6] + set[9] + 1) //2
set[9] = 0

print(max(set))
