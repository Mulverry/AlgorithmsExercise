function solution(sides) {
    let sideMax = Math.max(...sides);
    let sideMin = Math.min(...sides)
    let sideSum = sideMax + sideMin
    
    return sideSum-(sideMax-sideMin) -1
}