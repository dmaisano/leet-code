/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
  return () => n++ // ? https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
}
