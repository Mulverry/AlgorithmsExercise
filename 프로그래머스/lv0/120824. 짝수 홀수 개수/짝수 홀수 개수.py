from collections import Counter

def solution(num_list):
    odd, even = [], []
    for i in num_list:
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    answer = [len(even), len(odd)]
    return answer