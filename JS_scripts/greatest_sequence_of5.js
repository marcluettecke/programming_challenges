/**
 *Function so solve the following challenge from codewars:
 * Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.
 * @param digits String of digits
 * @returns {number} largest 5 long sequence of numbers in the string
 */
function solution(digits) {

    let result = 0
    for (let i = 0; i < digits.length; i++) {
        let current_slice = digits.slice(i, i + 5)
        if (current_slice.length === 5) {
            if (parseInt(current_slice) > result) {
                result = parseInt(current_slice)
            }

        }
    }
    return result
}

// console.log(validSequence("67790"))
solution("1234567800")
