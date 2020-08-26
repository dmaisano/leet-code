// https://leetcode.com/problems/max-consecutive-ones/

let findMaxConsecutiveOnes = (nums) => {
  let currentMax = 0,
    res = 0;

  for (num of nums)
    num === 1 ? (currentMax++, (res = Math.max(res, currentMax))) : (currentMax = 0);

  return res;
};

let x = [1, 1, 0, 1, 1, 1];
x = findMaxConsecutiveOnes(x);

console.log(x);
