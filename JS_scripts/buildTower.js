/**
 * Function to build a tower (or christmas tree) of depth nFloors
 * @param nFloors int for depth
 * @returns {[]} array of strings
 */
function towerBuilder(nFloors) {
    let max_length = nFloors * 2 - 1
    let stars
    let result = []
    for (let i = 1; i <= nFloors * 2; i += 2) {
        if (i === max_length) {
            stars = "*".repeat(i)

        } else {
            stars = " ".repeat(Math.floor((nFloors * 2 - i) / 2)) + "*".repeat(i) + " ".repeat(Math.floor((nFloors * 2 - i) / 2))
        }
        result.push(stars)
    }
    return result
}


console.log(towerBuilder(9))
