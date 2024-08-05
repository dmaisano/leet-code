import { describe, expect, it } from 'vitest'
import { checkIfInstanceOf } from './check-if-object-instance-of-class'

describe('checkIfInstanceOf', () => {
  it('should return true for a Date instance', () => {
    expect(checkIfInstanceOf(new Date(), Date)).toBe(true)
  })

  it('should return false for a non-instance', () => {
    expect(checkIfInstanceOf({}, Date)).toBe(false)
  })

  it('should return false for undefined and null literals', () => {
    expect(checkIfInstanceOf(null, null)).toBe(false)
    expect(checkIfInstanceOf(undefined, undefined)).toBe(false)
  })

  it('should return false for null', () => {
    expect(checkIfInstanceOf(null, Date)).toBe(false)
  })

  it('should return false for undefined', () => {
    expect(checkIfInstanceOf(undefined, Date)).toBe(false)
  })

  it('should return false if the second argument is not a function', () => {
    expect(checkIfInstanceOf(new Date(), {})).toBe(false)
  })

  it('should return true for an instance of a custom class', () => {
    class CustomClass {}
    const instance = new CustomClass()
    expect(checkIfInstanceOf(instance, CustomClass)).toBe(true)
  })

  it('should return true for primitive types', () => {
    expect(checkIfInstanceOf(42, Number)).toBe(true)
    expect(checkIfInstanceOf('wow, what a string!', String)).toBe(true)
  })

  it('should return true for an instance of a built-in class', () => {
    expect(checkIfInstanceOf([], Array)).toBe(true)
  })
})
