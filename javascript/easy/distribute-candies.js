// https://leetcode.com/problems/distribute-candies/

let distributeCandies = (candies) => {
  let sortNums = (a, b) => {
    return a - b;
  };
  let count = 1;

  candies = candies.sort(sortNums);

  for (let i = 1; i < candies.length && count < candies.length / 2; i++)
    if (candies[i] > candies[i - 1]) count++;

  return count;
};

let candies = [1, 1, 2, 2, 3, 3];
console.log(distributeCandies(candies));
