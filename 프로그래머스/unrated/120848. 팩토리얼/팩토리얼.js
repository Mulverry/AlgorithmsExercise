function solution(n) {
    let answer = 1
    for (let i=1; i<n+1; i++){
        answer *= i
        if (answer == n){
            return i
        }
        if (answer > n){
            return i-1
        }
    }


}