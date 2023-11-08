function solution(numbers) {
    numbers.sort((a,b)=>a-b)
    let ans1 = numbers[0]*numbers[1]
    let ans2 = numbers.at(-1)*numbers.at(-2)
    return ans1>ans2? ans1: ans2
    
}