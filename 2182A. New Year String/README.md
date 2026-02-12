# New Year String

## Problem Statement

A string consisting only of characters `0`, `2`, `5`, and `6` is called a **New Year string** if **at least one** of the following conditions is satisfied:

1. It contains `"2026"` as a continuous substring.
2. It does **not** contain `"2025"` as a continuous substring.

You are allowed to perform the following operation any number of times:

- Choose any character in the string and replace it with `0`, `2`, `5`, or `6`.

For each test case, compute the **minimum number of operations** required to make the string a New Year string.

---

## Input

- First line: integer `t` — number of test cases  
  ```
  1 ≤ t ≤ 10⁴
  ```
- For each test case:
- Integer `n` — length of string  
  ```
  4 ≤ n ≤ 20
  ```
- String `s` of length `n`, consisting only of `0, 2, 5, 6`

---

## Output

For each test case, print a single integer — the minimum number of operations required.

---

## Key Observations

A string is valid if:

- It already contains `"2026"` → answer is `0`
- OR it does not contain `"2025"` → answer is `0`

So operations are only needed when:
- `"2025"` exists
- AND `"2026"` does not exist

---

## Example

### Input

2025


Contains `"2025"` and not `"2026"`  
Minimum fix: change one character → e.g., `2225`  
Answer: `1`

---

## Complexity Analysis

For each test case:
- String length ≤ 20
- We check all substrings of length 4

### Time Complexity

O(t * n)


### Auxiliary Space

O(1)


Efficient for constraints.

---
