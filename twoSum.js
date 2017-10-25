/*
Given an numsay of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// Going under the assumption that each input will have exactly one solution
var twoSum = function(nums, target = undefined) {
  var res = [];

  if(target == undefined) {
    console.log("\nNo target value entered!\n");
    return;
  }
  
  for(var i = 0; i < nums.length; i++) {

    // iterates through the numbers as to ensure the same element is not selected twice
    for(var j = i + 1; j < nums.length; j++) {
      if(nums[j] == target - nums[i]) {
        res = [i, j]; // returns the indices of the two numbers whose addition == target
        break;
      }
    }
  }

  if(res == []) { // logs an error to the user should a solution not be found
    console.log("No numbers found that equal: " + target);
  }

  else {
    return res; // returns the resulting numsay
  }
};
