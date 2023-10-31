function solution(s) {
    var answer = 0;
    
    let stack = []
    let arr = s.split(' ')
    for (let i=0; i<arr.length; i++){
        arr[i] == "Z"? stack.pop() : stack.push(arr[i])
    }
    stack.map(v => v++).forEach(i => answer +=i)
    return answer
}