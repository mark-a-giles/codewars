var isSquare = (n) => {
    return (Math.sqrt(n) % 1) === 0;
}

let result = isSquare(5);
console.log(result);