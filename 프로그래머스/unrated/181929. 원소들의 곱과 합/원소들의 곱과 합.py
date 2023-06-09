import math

def solution(num_list):
    if math.prod(num_list) > math.pow(sum(num_list),2):
        return 0
    else:
        return 1