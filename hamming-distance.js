const hammingDistance = (x, y) => {
  // ^ bitwsise XOR operator
  let res = x^y;
  let distance; // hamming distance variable

  for(distance = 0; res > 0; distance++) {
    // &= bitwise AND operator
     res &= res - 1;
  }
  
  return distance;
};

let x = hammingDistance(1, 4);
x
