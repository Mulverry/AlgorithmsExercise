function solution(num_list) {
    let answer = num_list
    let last = num_list.at(-1)
    let second = num_list.at(-2)
    last > second? answer.push(last-second):answer.push(2*last)
    return answer
}