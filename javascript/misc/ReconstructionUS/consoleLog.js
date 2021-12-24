// reference to the default console prototypical object
const _myLogger = { ...console };

console.log = (obj) => {
  _myLogger.log(`${JSON.stringify(obj)} "${typeof obj}"`);
};

console.log(3); // 3 "number"
console.log(`a`); // "a" "string"
