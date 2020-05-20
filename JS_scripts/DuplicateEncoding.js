/**
 * Function to encode a string as a sting of "(" and ")" for either unique values or duplicate values, respectively
 * @param word string
 * @returns {string} encoded string
 */
function duplicateEncode(word){
  return word
    .toLowerCase()
    .split('')
    .map( function (a, i, w) {
      return w.indexOf(a) === w.lastIndexOf(a) ? '(' : ')'
    })
    .join('');
}

