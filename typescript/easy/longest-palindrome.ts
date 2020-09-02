// https://leetcode.com/problems/longest-palindrome/

function longestPalindrome(s: string): number {
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

    if (oddFound) {
      if (count > 1) {
        if (count % 2 == 0) {
          res += count;
        } else {
          // odd number of characters
          // subtract one to make it even and valid for the palindrome
          res += count - 1;
        }
      }
    } else {
      if (count % 2 == 0) {
        res += count;
      } else {
        // allows for a maximum of one odd character in the center of the palindrome
        res += count;
        oddFound = true;
      }
    }
  }

  return res;
}

console.log(longestPalindrome("dddcbabc"));
