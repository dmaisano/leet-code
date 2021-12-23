function longestCommonPrefix(strs: string[]): string {
  let prefix = "";
  const memo: string[] = [];

  for (const word of strs) {
    for (const char of word) {
      const newPrefix = prefix + char;

      const matches = strs.filter((x) => x.startsWith(newPrefix));

      // not all words have that prefix in common, move on to the next one
      if (matches.length !== strs.length) {
        memo.push(prefix);
        prefix = "";
      } else {
        prefix = newPrefix;
      }
    }
  }

  if (memo.length) {
    prefix = memo.reduce((word1, word2) =>
      word1.length > word2.length ? word1 : word2,
    );
  }

  return prefix;
}
