# Number of Ordered Pairs (a, b)

## Problem Statement
You are given an integer `n`.  
You need to find how many **ordered pairs** of positive integers `(a, b)` satisfy the condition:

a = n - b


---

## Input
- The first line contains an integer `t` — the number of test cases.
- Each test case contains one integer `n`.

**Constraints:**

1 ≤ t ≤ 99
2 ≤ n ≤ 100


---

## Output
- For each test case, print the number of ordered pairs `(a, b)`.

---

## Explanation
We need both `a` and `b` to be **positive integers**.  
Since `a = n - b`, for `a > 0` ⇒ `b < n`.  
And because `b` must be positive ⇒ `b ≥ 1`.

Thus, possible values of `b` are `1, 2, 3, …, n-1`.

Hence, the total number of valid ordered pairs = **n - 1**.

---

## Examples

### Example 1
**Input:**

3
2
4
6


**Output:**

1
3
5


**Explanation:**
- For `n = 2`: (a, b) = (1, 1)
- For `n = 4`: (a, b) = (3,1), (2,2), (1,3)
- For `n = 6`: (a, b) = (5,1), (4,2), (3,3), (2,4), (1,5)

---
