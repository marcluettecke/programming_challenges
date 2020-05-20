/**
 * Function to remove all occurrences of strings in array after the x'th occurrence. Clever use of filter function
 * and "or" operator
 * @param arr array of strings
 * @param x threshold of occurrences
 * @returns {*} new array of strings without the removed strings
 */
function deleteNth(arr, x) {
    let cache = {};
    return arr.filter(function (n) {
        cache[n] = (cache[n] || 0) + 1;
        return cache[n] <= x;
    });
}

console.log(deleteNth(['A', 'B', 'A', 'A', 'B'], 2))
