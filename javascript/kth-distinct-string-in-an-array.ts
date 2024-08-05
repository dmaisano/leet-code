export function kthDistinct(arr: string[], k: number): string {
  const frequencyMap: Map<string, number> = new Map()

  arr.forEach((str) => {
    frequencyMap.set(str, (frequencyMap.get(str) || 0) + 1)
  })

  const distinctStrings = arr.filter((str) => frequencyMap.get(str) === 1)

  return distinctStrings.length >= k ? distinctStrings[k - 1] : ''
}
