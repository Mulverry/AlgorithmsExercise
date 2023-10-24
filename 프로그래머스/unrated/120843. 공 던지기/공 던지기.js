function solution(numbers, k) {
    let getBall = 1
    while (k) {
        getBall +=2
        k--;
        if (getBall > numbers.length){
           numbers.length % 2 == 0 ? getBall = 1 : getBall = 2
        }
    }
    return getBall;
}