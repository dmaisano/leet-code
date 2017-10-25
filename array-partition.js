/*
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
*/

var arrayPairSum = function(nums) {
  var sum = 0;
  var res = [];

  var sortNums = (a,b) => { return a - b; }

  var min = (a, b) => {
    if(a < b) {
      return a;
    }
  
    return b;
  }

  nums.sort(sortNums);

  for(var i = 0; i < nums.length; i+=2) {
    res.push([ nums[i], nums[i+1] ]);
  }

  for(var i = 0; i < nums.length; i+=2) {
    sum += min(nums[i], nums[i+1]);
  }

  return sum;
};

var arr = [1,4,3,2];

var sum = arrayPairSum(arr);

console.log(sum + '\n');
