// https://leetcode.com/problems/longest-substring-without-repeating-characters/

function lengthOfLongestSubstring(word) {
  word = new Set(word);
  let res = 0;

  for (char of word) {
    res++;
  }

  return res;
}

let res = lengthOfLongestSubstring("pwwkew");

console.log(res);
