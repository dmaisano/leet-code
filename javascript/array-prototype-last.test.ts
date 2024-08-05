import { describe, it, expect } from 'vitest'
import './array-prototype-last'

describe('Array.prototype.last', () => {
  it('should return the last element of a non-empty array', () => {
    const arr = [1, 2, 3]
    expect(arr.last()).toBe(3)
  })

  it('should return -1 for an empty array', () => {
    const arr: number[] = []
    expect(arr.last()).toBe(-1)
  })

  it('should return the last element for an array with one element', () => {
    const arr = [42]
    expect(arr.last()).toBe(42)
  })

  it('should return the last element for an array with mixed types', () => {
    const arr = [1, 'two', { three: 3 }]
    expect(arr.last()).toEqual({ three: 3 })
  })

  it('should return the last element for an array with multiple types of elements', () => {
    const arr = ['apple', 'banana', 'cherry']
    expect(arr.last()).toBe('cherry')
  })
})
