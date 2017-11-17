# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

def findComplement(num):
  binaryNum = bin(num)[2:] # [2:] removes the '0b' from the string
  res = "";

  for bit in binaryNum:
    if(bit == '1'):
      res += '0'

    else:
      res += '1'

  return int(res, 2)
  
print(findComplement(5))
