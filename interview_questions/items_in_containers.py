from typing import List


"""
[Company] would like to know how much inventory exists in their closed inventory compartments. Given a string s consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk ('*' = ascii decimal 42)
A compartment is represented as a pair of pipes that may or may not have items between them ('|' = ascii decimal 124).


Example:
s = '|**|*|*'
startIndices = [1, 1]
endIndices = [5, 6]


The string, s, has a total of 2 closed compartments. One with 2 items and one with 1 item. For the first pair of indices, (1, 5), the substring is '|**|*'. There are 2 items in a compartment.

For the second pair of indices, (1, 6), the substring is '|**|*|' and there are 2 + 1 = 3 items in compartments.

Both of the answers are returned in an array,  [2, 3].

---

Function Description .

Complete the number_of_items function in the editor below. The function must return an integer array that contains the results for each of the startIndices[i] and endIndices[i] pairs.


number_of_items has three parameters:

  -  s: A string to evaluate

  -  startIndices: An integer array, the starting indices.

  -  endIndices: An integer array, the ending indices.

---

Constraints:

- 1 ≤ m, n ≤ 105
- 1 ≤ startIndices[i]  ≤ endIndices[i] ≤ n
- Each character of s is either '*' or '|'

---

Input Format For Custom Testing:

- The first line contains a string, s.
- The next line contains an integer, n, the number of elements in startIndices.
- Each line i of the n subsequent lines (where 1 ≤ i ≤ n) contains an integer, startIndices[i].
- The next line repeats the integer, n, the number of elements in endIndices.
- Each line i of the n subsequent lines (where 1 ≤ i ≤ n) contains an integer, endIndices[i].

---

Sample Case 0:


Sample Input For Custom Testing

STDIN         Function
-----         --------
*|*|      →   s = "*|*|"
1         →   startIndices[] size n = 1
1         →   startIndices = 1
1         →   endIndices[] size n = 1
3         →   endIndices = 3

Sample Output

0

Explanation

s = *|*|

n = 1

startIndices = [1]

n = 1

startIndices = [3]



The substring from index = 1 to index = 3 is '*|*'. There is no compartments in this string.

---

Sample Case 1:


Sample Input For Custom Testing

STDIN         Function
-----         --------
*|*|*|    →   s = "*|*|*|"
1         →   startIndices[] size n = 1
1         →   startIndices = 1
1         →   endIndices[] size n = 1
6         →   endIndices = 6

Sample Output:

2

Explanation

s = '*|*|*|'

n = 1

startIndices = [1]

n = 1

endIndices = [6]



The string from index = 1 to index = 6 is '*|*|*|'. There are two compartments in this string at (index = 2, index = 4) and (index = 4, index = 6). There are 2 items between these compartments.
"""


def number_of_items(
    s: str, startIndices: List[int], endIndices: List[int]
) -> List[int]:
    n = len(s)
    # prefix sum to store the count of '*' up to each position
    prefix_sum = [0] * (n + 1)
    left = [-1] * n
    right = [-1] * n

    # pre-compute prefix sum of '*'
    items_count = 0
    for i in range(n):
        if s[i] == "*":
            items_count += 1
        prefix_sum[i + 1] = items_count

    # pre-compute left nearest '|' positions
    left_pos = -1
    for i in range(n):
        if s[i] == "|":
            left_pos = i
        left[i] = left_pos

    # pre-compute right nearest '|' positions
    right_pos = -1
    for i in range(n - 1, -1, -1):
        if s[i] == "|":
            right_pos = i
        right[i] = right_pos

    result = []
    for i in range(len(startIndices)):
        start = startIndices[i] - 1
        end = endIndices[i] - 1

        # find the bounds of the compartment
        left_bound = right[start]
        right_bound = left[end]

        # if the bounds are valid and form a compartment
        if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
            result.append(prefix_sum[right_bound + 1] - prefix_sum[left_bound + 1])
        else:
            result.append(0)

    return result
