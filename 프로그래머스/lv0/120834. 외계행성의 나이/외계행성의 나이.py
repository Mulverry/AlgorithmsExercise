def solution(age):
    word = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    answer = ''
    for t in str(age):
        answer += word[int(t)]
    return answer