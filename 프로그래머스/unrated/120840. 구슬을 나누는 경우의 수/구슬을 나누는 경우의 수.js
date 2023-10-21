function solution(balls, share) {
    let answer = 1;
    if (share == 1 || balls-share == 1){
        answer = balls
    }else{
        while (share){
            answer *= balls/share 
            balls--;
            share--;
        }
    };
    return Math.round(answer)
}

// function solution(balls, share) {
//     var answer = facto(balls)/(facto(balls-share)*facto(share))
//     return answer
// }

// function facto(n){
//     if (n == 1) {return 1}
//     if (n>=2){
//         return n * facto(n-1)
//     }
// }