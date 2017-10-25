def findMedianSortedArrays(nums1 = [], nums2 = []):
  nums = []
  
  if nums1 != []:
    for num in nums1:
      nums.append(num)

  if nums1 != []:
    for num in nums2:
      nums.append(num)

  size = len(nums)
  # executes if the array contains an even number of elems
  if size % 2 == 0:
    median = (nums[int(size/2)] + nums[int((size/2)-1)]) / 2
  
  else:
    median = nums[int(size/2)]

  return median

x = [1,3]

z = findMedianSortedArrays(x)

print(z)
