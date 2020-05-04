/**
 * Function to address the codewars challenge:
 * The range of vision of a digit is its own value. 1 can see one digit to the left and one digit to the right,2 can see two digits, and so on.

 Thus, the loneliness of a digit N is the sum of the digits which it can see.

 Given a non-negative integer, your funtion must determine if there's at least one digit 1 in this integer such that its loneliness value is minimal.
 * @param number integer
 * @returns {boolean} if the integer 1 really returns the minimum value of left and right neighbors
 */
function loneliest(number) {
    let current_min = 99999
    let lowest_sum_with_1 = 99999
    let digit_list = Array.from(number.toString()).map(Number)
    let indicator_if_1 = false
    for (let i = 0; i < digit_list.length; i++) {
        let left_sum = 0
        for (let j = i - digit_list[i]; j < i; j++) {

            if (j >= 0) {
                left_sum += digit_list[j]
            }

        }
        let right_sum = 0
        for (let j = i + 1; j <= i + digit_list[i]; j++) {
            // console.log(digit_list[j])
            if (j < digit_list.length) {
                right_sum += digit_list[j]
            }
        }
        if (left_sum + right_sum <= current_min) {
            current_min = left_sum + right_sum
            indicator_if_1 = digit_list[i] === 1;
            if (indicator_if_1 === true) {
                lowest_sum_with_1 = current_min
            }
        }
    }
    return lowest_sum_with_1 === current_min
}
