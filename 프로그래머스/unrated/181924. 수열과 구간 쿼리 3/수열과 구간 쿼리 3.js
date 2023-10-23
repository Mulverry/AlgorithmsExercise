function solution(arr, queries) {
    var answer = arr;
    for (let i =0; i<queries.length; i++){
        let item = arr[queries[i][0]]
        answer[queries[i][0]] = answer[queries[i][1]]
        answer[queries[i][1]] = item
    }
    return answer
}