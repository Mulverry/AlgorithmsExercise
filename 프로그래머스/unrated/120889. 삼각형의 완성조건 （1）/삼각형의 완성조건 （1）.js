function solution(sides) {
    // let max = Math.max.apply(null, sides)
    let arr = sides.sort((a,b) => a-b)
    return arr.at(-1) < arr[0]+arr[1]? 1: 2
}