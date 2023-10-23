function solution(numbers, direction) {
    let answer = numbers;
    if (direction === "right"){
        answer.unshift(answer.pop())
    }else{
        answer.push(answer.shift())
    }
    return numbers;
}

// function solution(numbers, direction) {
//     direction === 'right' ? numbers.unshift(numbers.pop()) : numbers.push(numbers.shift());
//     return numbers;
// }