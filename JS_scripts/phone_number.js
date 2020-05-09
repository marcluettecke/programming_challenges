/**
 * Function to translate an array of length 9 into a phone number format (xxx) xxx-xxxx :
 * clever use of substrings
 * @param numbers Array of strings
 * @returns {string} phone number representation
 */
function createPhoneNumber(numbers){
  numbers = numbers.join('');
  return '(' + numbers.substring(0, 3) + ') '
      + numbers.substring(3, 6)
      + '-'
      + numbers.substring(6);
}
