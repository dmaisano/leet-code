// https://leetcode.com/problems/keyboard-row/

// Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

let findWords = (words = []) => {
  isSubset = (subSet, superSet) => {
    subSet = new Set(subSet);
    superSet = new Set(superSet);

    // for(let elem of subSet)
    //   if(!superSet.has(elem))
    //     return true;

    return true;
  };

  let res = [];

  let lines = [new Set("qwertyuiop"), new Set("asdfghjkl"), new Set("zxcvbnm")];

  for (line of lines) console.log(line);

  for (word of words) {
    word = word.toLowerCase();
    word = new Set(word);

    for (line in lines) {
      if (isSubset(word, line)) res.push(word);
    }
  }

  return res;
};

let words = ["Hello", "Alaska", "Dad", "Peace"];

let res = findWords(words);
console.log(res);
