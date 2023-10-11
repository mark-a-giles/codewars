function duplicateCount(text) {
    let count = 0;
    let char_map = {};
    for (let char of text) {
        char = char.toLowerCase();
        if (!char_map.hasOwnProperty(char)) {
            char_map[char] = 1;
        } else {
            char_map[char]++;
        }
    }
    for (let char of Object.keys(char_map)) {
        if (char_map[char] > 1) {
            count++;
        }
    }
    return count;
}

let r1 = duplicateCount('aabbcdeA');
let r2 = duplicateCount('Indivisibilities');

console.log(r1, r2);