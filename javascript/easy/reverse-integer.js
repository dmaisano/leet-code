// https://leetcode.com/problems/reverse-integer/

/**
 * @param {number} x
 * @return {number}
 */
let reverse = function (x) {
  let xString = x.toString();

  let isNegative = false;
  if (xString.includes("-")) {
    isNegative = true;
  }

  xString = xString.match(/\d+/g)[0];

  let tmp = "";
  for (let i = xString.length - 1; i >= 0; i--) {
    tmp += xString[i];
  }

  if (isNegative) {
    tmp = `-${tmp}`;
  }

  return parseInt(tmp, 10);
};
