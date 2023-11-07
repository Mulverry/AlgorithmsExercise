function solution(n) {
    return n.toString().split('').map(i => Number(i)).reduce((a,b) => a+b);
}