function solution(numbers, k) {
    while (k-1) {
        numbers.push(numbers.shift())
        numbers.push(numbers.shift())
        k--;    
    }
    return numbers[0];
}