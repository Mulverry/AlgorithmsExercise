function solution(numbers) {
    let arr = numbers.sort((comp1, comp2)=>comp1-comp2)
    var answer = arr.at(-1) * arr.at(-2);
    return answer;
}