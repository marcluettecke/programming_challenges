/**
 * Function to generate a series from m to n (inclusive)
 * @param m startpoint of array
 * @param n endpoint of array
 * @returns {number[]} array runnign from m to n
 */
function generateIntegers(m, n) {
    //first create array object of specific length and then fill it with subsequent values. clever one-liner
    return Array(n - m + 1).fill().map(() => m++);
}
