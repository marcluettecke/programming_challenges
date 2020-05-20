/**
 * Returns the difference of two arrays (also removes all duplicate values)
 * @param a array from which values to be removed
 * @param b array of values to remove
 * @returns {*} difference between the two
 */
function array_diff(a, b) {
  return a.filter(e => !b.includes(e));
}
