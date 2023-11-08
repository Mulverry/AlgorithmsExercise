function solution(my_string) {
    return [...my_string].map(i => i.toLowerCase()).sort().join("");
}