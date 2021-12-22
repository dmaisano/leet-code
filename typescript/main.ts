import { default as validParentheses } from "./easy/valid-parentheses";

export const main = async () => {
  console.log(validParentheses(`({[{[]}]})`));
};

main().catch(console.error);
