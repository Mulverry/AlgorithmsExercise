def solution(emergency):
    answer = []
    cmp = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(cmp.index(i)+1) 
    return answer