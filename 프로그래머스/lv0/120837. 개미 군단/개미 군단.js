function solution(hp) {
    var answer = 0;
    answer += parseInt(hp / 5);
    answer += parseInt((hp % 5) / 3)
    if ((hp % 5)%3 != 0){
        answer += (hp % 5) % 3
    }
    return answer;
}