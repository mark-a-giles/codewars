function reverseWords(str) {
    var string_array = str.split(/(\s+)/);
    for (let i = 0; i < string_array.length; i++) {
        let word = string_array[i];
        if (!word.match(/(\s+)/)) {
            string_array[i] = word.split('').reverse().join('');
        }
    }
    return string_array.join('');
}

var str   = "my car is red";
let result = reverseWords(str);
console.log(result);