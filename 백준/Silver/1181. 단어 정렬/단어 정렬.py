import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n):
    word = sys.stdin.readline().strip() ## 오답이유: sys.stdin.readline().strip() 모름.
    word_list.append(word)

set(word_list) # 집합으로 바꿔서 중복 제거

set_words = list(set(word_list))

set_words.sort()
set_words.sort(key = len) # 우선되는 기준을 나중에 정렬

for i in set_words:
    print(i)