function solution(my_string) {
    let numbers = my_string.replace(/[A-z]/g, " ")
                            .split(" ")
                            .map(i => Number(i))
    return numbers.reduce((a,b) => a+b)
}