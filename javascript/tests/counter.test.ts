import { describe, expect, it } from 'vitest'
import { createCounter } from '../counter'

describe('createCounter', () => {
  it('should return a function that increments the counter', () => {
    const counter = createCounter(10)

    expect(counter()).toBe(10)
    expect(counter()).toBe(11)
    expect(counter()).toBe(12)
  })

  it('should create independent counters', () => {
    const counter1 = createCounter(5)
    const counter2 = createCounter(20)

    expect(counter1()).toBe(5)
    expect(counter1()).toBe(6)
    expect(counter2()).toBe(20)
    expect(counter2()).toBe(21)
  })

  it('should handle negative starting values', () => {
    const counter = createCounter(-5)

    expect(counter()).toBe(-5)
    expect(counter()).toBe(-4)
  })

  it('should handle zero as a starting value', () => {
    const counter = createCounter(0)

    expect(counter()).toBe(0)
    expect(counter()).toBe(1)
  })
})
