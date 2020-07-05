encoder = {
    a: 1,
    e: 2,
    i: 3,
    o: 4,
    u: 5
}

/**
 * Function to encode ALL  vowels in a string with numeric values and back. Interesting use of global option and
 * RegExp in string.replace method
 * @param string input string
 * @returns {*} output string
 */
function encode(string) {
    for (let x in encoder){
        string = string.replace(new RegExp(x, "g"), encoder[x])
    }
    return string
}

function decode(string) {
    for (let x in encoder){
        string = string.replace(new RegExp(encoder[x], "g"), x)
    }
    return string
}
