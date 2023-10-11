function solution(str, ending){
    return (str.substring(str.length - ending.length) === ending);
}
let s1 = solution('abc', 'bc') // returns true
let s2 = solution('abc', 'd') // returns false

console.log(s1, s2);