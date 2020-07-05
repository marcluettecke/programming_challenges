/**
 * Function to return the sum of all permuted values of an input number
 * @param inputNumber int (potentially large) as basis for sum calculations
 * @returns {number} sum of all permutations
 */
const permutator = (inputNumber) => {
    let inputArr = (inputNumber+"").split("")
    console.log(inputArr)
    let result = [];

    const permute = (arr, m = []) => {
        if (arr.length === 0) {
            result.push(m)
        } else {
            for (let i = 0; i < arr.length; i++) {
                let curr = arr.slice();
                let next = curr.splice(i, 1);
                permute(curr.slice(), m.concat(next))
            }
        }
    }

    permute(inputArr)

    function getSum(total, num) {
        return total + Math.round(num);
    }
    return result.map(e => Number(e.join(""))).reduce(getSum, 0)
}

console.log(permutator(10**20))
