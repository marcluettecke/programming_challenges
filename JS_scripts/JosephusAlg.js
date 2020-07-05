/**
 * Solution to the Josephus problem (given a group of n people, they kill themselves, every k'th one until the last
 * one commits suicide.
 * Smart use of push and shift to always start at different position of array.
 * @param items array item
 * @param k skip sequence
 * @returns {[]} array with order of deaths
 */
function josephus(items, k) {
    let deathOrder = [];
    while (items.length !== 0) {
        for (let skip = 1; skip < k; skip++) items.push(queue.shift());
        deathOrder.push(items.shift());
    }
    return deathOrder
}

/**
 * Solution to the Josephus problem (given a group of n people, they kill themselves, every k'th one until the last
 * one commits suicide.
 * Smart use of modulo and condition to push items to result array.
 * @param items array item
 * @param k skip sequence
 * @returns {[]} array with order of deaths
 */
function josephus(items, k) {
  let i = 1, result = [];
  while (items.length)
    items = items.filter(item => i++ % k || !result.push(item));
  return result;
}


