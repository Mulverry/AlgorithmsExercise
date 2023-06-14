from collections import Counter

def solution(num_list):
    # odd, even = [], []
    # for i in num_list:
    #     if i % 2 == 1:
    #         odd.append(i)
    #     else:
    #         even.append(i)
    # answer = [len(even), len(odd)]
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer