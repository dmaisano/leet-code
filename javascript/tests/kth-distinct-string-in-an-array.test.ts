import { describe, expect, it } from 'vitest'
import { kthDistinct } from '../kth-distinct-string-in-an-array'

describe('kthDistinct', () => {
  it('should return the k-th distinct string when there are enough distinct strings', () => {
    expect(kthDistinct(['d', 'b', 'c', 'b', 'c', 'a'], 2)).toBe('a')
    expect(kthDistinct(['aaa', 'aa', 'a'], 1)).toBe('aaa')
  })

  it('should return an empty string when there are fewer than k distinct strings', () => {
    expect(kthDistinct(['a', 'b', 'a'], 3)).toBe('')
  })

  it('should handle arrays with all distinct strings', () => {
    expect(kthDistinct(['x', 'y', 'z'], 2)).toBe('y')
    expect(kthDistinct(['x', 'y', 'z'], 3)).toBe('z')
  })

  it('should handle arrays with no distinct strings', () => {
    expect(kthDistinct(['a', 'a', 'b', 'b'], 1)).toBe('')
  })

  it('should handle arrays with mixed distinct and non-distinct strings', () => {
    expect(kthDistinct(['a', 'b', 'c', 'a', 'd', 'c'], 2)).toBe('d')
  })

  it('should return the correct distinct string for larger values of k', () => {
    expect(kthDistinct(['a', 'b', 'a', 'c', 'b', 'd', 'e'], 3)).toBe('e')
  })

  it('should return an empty string for out of bounds k', () => {
    expect(kthDistinct(['a', 'b', 'c'], 4)).toBe('')
  })
})
