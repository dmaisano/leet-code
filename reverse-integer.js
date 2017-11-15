let reverse = (x) => {
  let res = 0;

  while(x) {
    let temp = (res * 10) + (x % 10);

    if(temp / 10 != res)
      return 0;

    res = temp;
    x /= 10;
  }

  return res;
};

let num = 123;
// reverse(num);
console.log(reverse(num));
