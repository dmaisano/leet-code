// https://leetcode.com/problems/fizz-buzz/

let fizzBuzz = (n) => {
  let res = [];

  for (let x = 1; x <= n; x++) {
    if (x % 3 == 0 && x % 5 != 0) res.push("Fizz");
    else if (x % 5 == 0 && x % 3 != 0) res.push("Buzz");
    else if (x % 3 == 0 && x % 5 == 0) res.push("FizzBuzz");
    else res.push(x.toString());
  }

  return res;
};

let n = 15;
console.log(fizzBuzz(n));
