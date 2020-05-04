/**
 * Solution to the question with a demonstration of the map function JS to apply a method to every element in an array
 * Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

 For example: ["3:1", "2:2", "0:1", ...]

 Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

 if x>y - 3 points
 if x<y - 0 point
 if x=y - 1 point
 * @param games array of strings indicating a score, such as "1:0"
 * @returns {number} of total score
 */
function points(games) {
    let total = 0;
    games.map(game => {
        if (game[0] === game[2]) {
            total += 1;
        } else if (game[0] > game[2]) {
            total += 3;
        }
    });
    return total;
}
