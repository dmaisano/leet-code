// https://leetcode.com/problems/robot-return-to-origin/

// moves is a string (ex) "UL" // up & left
let judgeCircle = (moves) => {
  let pos = [0, 0]; // position the player chooses to move
  // pos[0] = x-cord
  // pos[1] = y-cord

  for (move of moves) {
    if (move == "U") pos = [pos[0], ++pos[1]];
    else if (move == "D") pos = [pos[0], --pos[1]];
    else if (move == "L") pos = [--pos[0], pos[1]];
    else if (move == "R") pos = [++pos[0], pos[1]];
  }

  if (pos[0] == 0 && pos[1] == 0) return true;

  return false;
};

console.log(judgeCircle("UD"));
