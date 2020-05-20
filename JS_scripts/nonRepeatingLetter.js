/**
 * Function to find the first non-repeating letter in string with use of array.find and str.match (regex)
 * expressions with length 1
 * @param str
 * @returns {T | string} either the first none repeating letter or none
 */
function firstNonRepeatingLetter(str) {
    return str.split('').find(e => str.match(new RegExp(`${e}`, 'gi')).length === 1) || ''
}
