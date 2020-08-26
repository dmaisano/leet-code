// https://leetcode.com/problems/median-of-two-sorted-arrays/

let findMedianSortedArrays = (nums1 = [], nums2 = []) => {
  let sortNums = (a, b) => {
    return a - b;
  };
  let nums = nums1.concat(nums2).sort(sortNums);
  let len = nums.length;

  if (len % 2 == 0) {
    let index = len / 2;
    return (nums[--index] + nums[++index]) / 2;
  } else {
    let index = Math.round(nums.length / 2) - (len % 2);
    return nums[index];
  }
};
