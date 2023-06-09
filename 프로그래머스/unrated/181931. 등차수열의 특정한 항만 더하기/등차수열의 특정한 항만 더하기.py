def solution(a, d, included):
    arr = []
    n = len(included)
    index = []
    answer = 0
    
    for i in range(n):
        arr.append(a + i * d)
    
    for j in range(n):
        if included[j] == True:
            answer += arr[j]
        
    return answer