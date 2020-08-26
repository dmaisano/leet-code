// https://leetcode.com/problems/next-greater-element-i/

let nextGreaterElement = (nums1, nums2) => {
  let res = [];

  for (i in nums1) {
    if (nums1[i] < nums2[i]) res.push(nums2[i]);
    else res.push(-1);
  }

  return res;
};
