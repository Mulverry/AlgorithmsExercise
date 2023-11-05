function solution(array, n) {
    let answer = []
    array.sort((a, b)=> Math.abs(n-a) - Math.abs(n-b) || a-b)
    
    return array[0];
}