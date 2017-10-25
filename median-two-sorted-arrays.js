var findMedianSortedArrays = function(nums1 = [], nums2 = []) {
  var nums = [];
  var median = 0;

  // pushes the values to the new array
  if(nums1 != []) {
    for(var i = 0; i < nums1.length; i++) {
      nums.push(nums1[i]);
    }
  }

  if(nums2 != []) {
    for(var i = 0; i < nums2.length; i++) {
      nums.push(nums2[i]);
    }
  }

  var len = nums.length;

  // executes if the array contains an even number of elems
  if(len % 2 == 0) {
    // ex (2+3)/2 = 2.5
    median = (nums[(len/2)-1] + nums[(len/2)])/2
  }

  else {
    median = nums[len/2];
  }

  return median;
};

let x = [1,3];

console.log(findMedianSortedArrays(x));
