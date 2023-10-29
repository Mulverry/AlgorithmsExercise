function solution(my_string) {
    let numbers = my_string.replace(/[^0-9]/g, '')
    var answer = [...numbers].map((i)=> Number(i)).sort()
    return answer;
}