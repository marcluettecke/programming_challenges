const rgb = (r, g, b) => toHex(r) + toHex(g) + toHex(b);

/**
 * Clever function to convert three integer rgb to hex code
 * @param numb
 * @returns {string}
 */
function toHex(numb) {
  if (numb <= 0)   return '00';
  if (numb > 255)  return 'FF';
  return numb.toString(16).toUpperCase();
}
