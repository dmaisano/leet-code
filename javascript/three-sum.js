var threeSum = function(nums) {
  var triplets = [];

  // sorts the array arg numerically
  var sortNums = (a,b) => { return a - b; }

  nums.sort(sortNums);

  // iterates through the nums array
  for(var i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] == nums[i-1]) {
      continue;
    }

    var left = i + 1, right = nums.length - 1;

    while(left < right) {
      // temp = a + b + c
      var temp = nums[i] + nums[left] + nums[right];

      if(temp < 0) {
        left += 1; // increment the left
      }

      else if(temp > 0) {
        right -= 1; // decrement the right
      }

      else { // if a + b + 
        // pushes the new array to the "triplets"
        triplets.push([nums[i], nums[left], nums[right]])
      }

      while (left < right && nums[left] == nums[left+1]) {
        left += 1; // increment the left
      }
        

      while (left > right && nums[left] == nums[right-1]) {
        right += 1; // decrement the right
      }

      left += 1 // increment the left
      right -= 1 // decrement the right
    }
  }

  return triplets;
}

var values = [-1, 0, 1, 2, -1, -4];
values = threeSum(values);

for(i in values) {
  console.log(values[i]);
}
