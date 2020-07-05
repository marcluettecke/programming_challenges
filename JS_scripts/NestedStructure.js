/**
 * Solution to Complete the function/method (depending on the language) to return true/True when its argument is an
 * array that has the same nesting structure as the first array. Clever use of prototype functions and recursion.
 * @param other array to check structure against
 * @returns {boolean}
 */
Array.prototype.sameStructureAs = function (other) {
    //exit criterion if overall length is already not the same
    if (!Array.isArray(other) || this.length !== other.length)
        return false;
    // check for every element the substructure
    for (let i = 0; i < this.length; ++i) {
        if (Array.isArray(this[i])) {
            // recursive portion
            if (!this[i].sameStructureAs(other[i])) {
                return false;
            }
        } else if (Array.isArray(other[i])) {
            return false;
        }
    }
    // if all checks fails, then return true
    return true;
};
