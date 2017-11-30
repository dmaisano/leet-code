let calPoints = (ops) => {
  let scores = [];
  let count = 0;
  let sum = 0;

  for(i in ops) {
    if(!isNaN(ops[i])) {
      scores.push(Number(ops[i]));
    }

    if(ops[i] === '+' && scores.length >= 2) {
      scores.push(scores[scores.length-1] + scores[scores.length-2]);
    }
    
    else if(ops[i] === '+' && scores.length < 2) {
      console.log('Invalid Operation, need two valid scores to get the sum!');
    }

    if(ops[i] === 'D') {
      scores.push(scores[scores.length-1] * 2);
    }

    if(ops[i] === 'C') {
      scores.pop();
    }
  }

  for(score of scores) {
    sum += score;
    console.log(`Round ${++count}: You could get ${score} points. The sum is: ${sum}`);
  }

  return sum;
};

let test = ['5', '2', 'C', 'D', '+'];
calPoints(test);
