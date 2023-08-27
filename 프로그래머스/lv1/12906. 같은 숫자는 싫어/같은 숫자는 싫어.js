function solution(arr)
{
    var answer = [];
    
    for (let i = 0; i < arr.length; i++){
        answer.push(arr[i])
        if (arr[i] === arr[i-1]){
            answer.pop(arr[i])
        }
    } 

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('answer')
    
    return answer;
}