/**
 * Function replace elements in an 100-element, starting at 1, Array with strings if they are divisible by predefined
 * numbers
 * Good example of use of map function
 * @param string1 string to replace the elements of array with that are divisible by num1
 * @param string2 string to replace the elements of array with that are divisible by num2
 * @param num1 int to check divisibility of elements for string1
 * @param num2 int to check divisibility of elements for string2
 * @returns {unknown[]}
 */
const fizzBuzzCustom = (string1 = 'Fizz', string2 = 'Buzz', num1 = 3, num2 = 5) => {
    return Array.from(new Array(100), (nums, i) => i + 1).map((num) => {
        if (!(num % (num1 * num2))) return string1 + string2;
        else if (!(num % num1)) return string1;
        else if (!(num % num2)) return string2;
        else return num;
    })
}
