// https://leetcode.com/problems/add-two-numbers/

var addTwoNumbers = function (l1, l2) {
  let res = [];
  var sum = 0;

  for (var i = 0; i < l1.length; i++) {
    sum = l1[i] + l2[i];

    if (sum) res.push(sum);
  }

  return res;
};

let x = [2, 4, 3];
let y = [5, 6, 4];

let z = addTwoNumbers(x, y);

console.log(z);
