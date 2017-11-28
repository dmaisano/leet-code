let reverseWords = (str) => {
  str = str.split(' ');
  let res = '';

  for(let i = str.length-1; i >= 0; i--) {
    if(str[i] != ' ') {
      res += str[i]
    }

    if(i != str.length-1 || i != 0) {
      res += ' ';
    }
  }

  return res;
};

let words = 'the sky is blue';
let x = " ";
console.log(reverseWords(words));
