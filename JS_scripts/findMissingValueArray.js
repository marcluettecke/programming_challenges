/**
 * Function to find the missing value in a (large) unordered array of consecutive numbers. Clever use of iterator
 * with open end and array.includes method.
 * Example:
 * array = [1,5,3,2]
 * returns = 4
 * @param array of integers
 * @returns {number} missing number
 */
function findNumber(array) {
    for (var i = 1; ; i++) if (!array.includes(i)) return i
}
