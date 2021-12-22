function isValid(s: string): boolean {
  const openingBrackets = `({[`;
  const closingBrackets = `)}]`;

  // ? map I will use to determine if a pair of brackets is a match
  const matchingBrackets: {
    [key: string]: string;
  } = {
    ")": "(",
    "}": "{",
    "]": "[",
  };

  const stack: string[] = [];

  for (const char of s) {
    // ? push all the opening brackets to the stack
    if (openingBrackets.includes(char)) {
      stack.push(char);
    }
    // ? we found a closing bracket, check if valid
    else if (closingBrackets.includes(char)) {
      if (stack.length === 0) {
        return false; // ? invalid operation
      }

      const top = stack[stack.length - 1];
      if (top === matchingBrackets[char]) {
        stack.pop();
      } else {
        return false; // ? bracket mis-match
      }
    }
  }

  return stack.length === 0;
}

export default isValid;
