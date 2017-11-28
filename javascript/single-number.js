// let singleNumber = (arr) => {
//   let set = new Set(arr);
//   let res = new Set();

//   for(x in arr)
//     for(y in arr)
//       if(x != y && arr[x] == arr[y])
//       res.add(arr[y]);

//   for(elem of set)
//     if(!res.has(elem))
//       return elem;

//   return false;
// };

let singleNumber = (nums) => {
  let sum = (nums) => {
    let total = 0;

    for(num of nums)
      total += num;

    return total;
  }

  let set = [...new Set(nums)];

  return 2 * sum(set) - sum(nums);
};
  
console.log(singleNumber([]));
console.log(singleNumber([1, 1, 1, 2]));
console.log(singleNumber([1, 2, 3, 1, 2, 1]));
