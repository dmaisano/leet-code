// https://leetcode.com/problems/reverse-words-in-a-string/

// need to preserve whitespace

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  return s.split(" ").reverse().join(" ");
};
