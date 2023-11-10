function solution(s1, s2) {
    var answer = 0;
    s1.map(i => s2.includes(i)? answer += 1 : 0)
    return answer;
}