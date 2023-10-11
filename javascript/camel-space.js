function solution(string) {
    string = string.split('');
    for (let i = string.length - 1; i >= 0; i--) {
        if (string[i].match(/[A-Z]/)) {
            string.splice(i, 0, ' ');
        }
    }
    return string.join('');
}

let result = solution('camelCasingTest');
let r2 = solution('camelCasing');

console.log(result, r2);