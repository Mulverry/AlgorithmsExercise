function solution(dots) {
    let answer = 0;
    dots.sort()
    let width = Math.abs(dots[0][0] - dots[2][0])
    let length = Math.abs(dots[0][1] - dots[1][1])
    return width*length;
}