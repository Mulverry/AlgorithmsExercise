function solution(hp) {
    var answer = 0;
    answer += parseInt(hp / 5);
    answer += parseInt((hp % 5) / 3)
    if ((hp % 5)%3 != 0){
        answer += (hp % 5) % 3
    }
    return answer;
}

function solution(hp) {
    const 장군개미 = Math.floor(hp / 5);
    const 병정개미 = Math.floor((hp - (장군개미 * 5)) / 3);
    const 일개미 = hp - ((장군개미 * 5) + (병정개미 * 3));
    return 장군개미+병정개미+일개미;
}
