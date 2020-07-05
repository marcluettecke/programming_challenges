/*
Solution to a problem to capitalize elements of a string if index occurs in inpout array
 */

/**
 *
 * @param input_string
 * @param capitalize_array
 * @returns {string}
 */
function capitalize(input_string, capitalize_array) {
    let result_array = []
    input_string.split("").forEach((char, index) => {
            if (capitalize_array.includes(index)){
                result_array.push(char.toUpperCase())
            }
            else {
                result_array.push(char)
            }

        }
    )
    return result_array.join("")
}

/*
Short solution with clever use of map function and either or operator
 */
function capitalize_short(s,arr){
  return [...s].map((x,i)=>arr.includes(i)?x.toUpperCase():x).join('')
};

