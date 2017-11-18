let calPoints = (ops) => {
  let sum = 0;

  for(let i = 0; i <= ops.length; i++) {
    if(!isNaN(ops[i])) {
      sum += Number(ops[i]);
      console.log("Round " + ++i + " You could get " + ops[i] + " points. The sum is: " + sum);
    }
  }
};

let test = ["5","2"];
calPoints(test);
