// Sum Numbers
function sum (numbers) {
    let sum = 0;
    if (numbers.length === 0) {
      return 0;
    }
    numbers.forEach( num => {
        sum += num;
    })
    return sum;
};