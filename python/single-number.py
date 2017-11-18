def singleNumber(nums):
  a = 0
  for i in nums:
      a ^= i
  return a

print(singleNumber([1, 1, 1, 2]))
