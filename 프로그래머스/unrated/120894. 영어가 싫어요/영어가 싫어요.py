def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)