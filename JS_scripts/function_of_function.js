/**
 * Function to answer the following challenge wth smart if else abbrevations and nested functions:
 *This time we want to write calculations using functions and get the results. Let's have a look at some examples:

 seven(times(five())); // must return 35
 four(plus(nine())); // must return 13
 eight(minus(three())); // must return 5
 six(dividedBy(two())); // must return 3
 Requirements:

 There must be a function for each number from 0 ("zero") to 9 ("nine")
 There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
 Each calculation consist of exactly one operation and two numbers
 The most outer function represents the left operand, the most inner function represents the right operand
 Divison should be integer division. For example, this should return 2, not 2.666666...:
 */
['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    .forEach(function (name, n) {
        this[name] = function (f) {
            return f ? f(n) : n
        }
    });

function plus(n) {
    return function (a) {
        return a + n
    }
}

function minus(n) {
    return function (a) {
        return a - n
    }
}

function times(n) {
    return function (a) {
        return a * n
    }
}

function dividedBy(n) {
    return function (a) {
        return a / n
    }
}
