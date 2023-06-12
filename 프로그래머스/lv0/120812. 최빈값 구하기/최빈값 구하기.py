from collections import Counter

def solution(array):
    count = Counter(array).most_common()
    if len(count) == 1:
        answer = count[0][0]
    else:
        if (count[0][1] == count[1][1]):
            answer = -1
        else:
            answer = count[0][0]
    return answer

# cnt = [0] * (len(array) + 1)
#     for i in array:
#         cnt[i] += 1
    
#     cnt.sort()
#     if cnt[-1] == cnt[-2]:
#         answer = -1
#     else:
#         answer = max(cnt)