/**
 * Function to redefine an age integer to either 20 or 21 based on a different number system
 * @param n original age
 * @returns {string} String expression stating age, new age and the used base
 */
function womensAge(n) {
  return `${n}? That's just ${20+n%2}, in base ${Math.floor(n/2)}!`
}
