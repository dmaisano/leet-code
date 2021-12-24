function getPairs(obj) {
  // I could have probably done this in a fancy javascript one-liner, but opted not to. For practical purposes I'd rather showcase something like this that is more readable and easy to follow
  const pairs = [];

  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === `object`) {
      // nested object found, making a recursive call to extract the key/value pair inside
      pairs.push(...getPairs(value));
    } else if (typeof value !== `object`) {
      pairs.push([key, value]);
    }
  }

  return pairs;
}

// const res = getPairs({
//   a: 1,
//   b: {
//     c: 2,
//     d: {
//       e: 2,
//     },
//   },
//   c: { d: 3 },
// });

const res = getPairs({
  a: 1,
  b: {
    c: 2,
    d: {
      e: {
        f: {
          g: 10,
          h: 20,
          i: 30,
        },
      },
    },
  },
  c: { d: 3 },
});

console.log(res);

// should return
// [['a',1],['c',2],['e',2],['d',3]]
