function createCounter(n: number): () => number {
  return () => n++ // ? https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
}

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
