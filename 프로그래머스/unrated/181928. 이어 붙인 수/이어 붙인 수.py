def solution(num_list):
    even = []
    odd = []
    for i in num_list:
        if i % 2 == 1:
            odd.append(str(i))
        else:
            even.append(str(i))
    answer = int(''.join(odd)) + int(''.join(even))
    return answer