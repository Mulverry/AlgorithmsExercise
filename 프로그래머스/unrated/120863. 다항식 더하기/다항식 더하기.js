function solution(polynomial) {
    var answer = [];
    let xNum = 0;
    let num = 0;
    let arr = polynomial.split(' + ')
    arr.forEach((i) => {
        if (i.includes("x")){
            let removeX = i.replace("x","") || "1"
            xNum += parseInt(removeX)
        } else {
            num += Number(i)
        }
    })
    if (xNum != 0 && num != 0){
        xNum == 1? answer = `x + ${num}` : answer = `${xNum}x + ${num}`
    } else if (xNum != 0 && num == 0){
        xNum == 1? answer = `x` : answer = `${xNum}x`
    } else if (xNum == 0 && num !=0){
        answer = `${num}`
    }
    return answer;
}