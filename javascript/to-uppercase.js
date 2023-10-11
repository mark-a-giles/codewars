String.prototype.toJadenCase = function () {
    let jaden_string = [];
    for (let word of this.split(' ')) {
        jaden_string.push(word.charAt(0).toUpperCase() + word.slice(1));
    }
    return jaden_string.join(' ');
};
let name = 'Mark is doing this task.';
console.log(name.toJadenCase())