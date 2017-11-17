let longestWord = (words) => {
  let indices = [];

  for(word of words) {
    indices.push(word.length);
  }

  let max = Math.max.apply(null, indices);

  for(word of words) {
    if(word.length == max)
      return word;
  }
};

let x = ["w","wo","wor","worl", "world"];
x = longestWord(x);

console.log(x);
