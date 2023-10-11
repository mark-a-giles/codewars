function getDivisorsCnt(n) {
    let divisors = 0;
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i == 0) {
            if (n / i == i) {
                divisors++;
            } else {
                divisors = divisors + 2;
            }
        }
    }
    return divisors;
}
let r = getDivisorsCnt(11);
let r2 = getDivisorsCnt(8);
console.log(r, r2);
