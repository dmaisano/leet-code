// https://leetcode.com/problems/longest-palindrome/

let longestPalindrome: (s: string) => number;

// slow solution
longestPalindrome = (s: string): number => {
  // count of all the characters in the string
  const charCounts: {
    [key: string]: number;
  } = {};

  for (const char of s) {
    charCounts[char] == null ? (charCounts[char] = 1) : charCounts[char]++;
  }

  let res: number = 0;
  let oddFound: boolean = false;
  for (const char in charCounts) {
    const count = charCounts[char];

    if (count % 2 === 0) {
      res += count;
    } else {
      if (oddFound) {
        res += count - 1;
      } else {
        // found the first odd character
        oddFound = true;
        res += count;
      }
    }
  }

  return res;
};

// optimized solution (only slightly faster)
longestPalindrome = (s: string): number => {
  // count of all the characters in the string
  const charCounts: {
    [key: string]: number;
  } = {};

  for (const char of s) {
    charCounts[char] == null ? (charCounts[char] = 1) : charCounts[char]++;
  }

  let res: number = 0;
  for (const char in charCounts) {
    const count = charCounts[char];

    // adds the greatest maximum occurence of even characters
    res += ~~(count / 2) * 2;

    // found first occurence of odd characters
    if (res % 2 === 0 && count % 2 === 1) {
      res += 1;
    }
  }

  return res;
};

console.log({
  "longest palindrome": longestPalindrome("abccccdd"), // 7
});
