function solution(my_string) {
    let numbers = my_string.replace(/[^0-9]/g, '')
    let ans = 0 ; 
    for (let i=0; i<numbers.length; i++){
        ans += Number(numbers[i])
    }
    return ans;
}