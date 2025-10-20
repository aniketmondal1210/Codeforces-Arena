# Last Two Digits of 5ⁿ

## Problem Statement
You are given a single integer `n`.  
Your task is to compute the **last two digits** of the number `5ⁿ`.

---

## Input
A single integer:

n (2 ≤ n ≤ 2 × 10¹⁸)


---

## Output
Print the **last two digits** of `5ⁿ` **without spaces**.

---

## Explanation
Let’s observe the pattern for powers of 5:

| n | 5ⁿ | Last Two Digits |
|---|----|-----------------|
| 1 | 5 | 05 |
| 2 | 25 | 25 |
| 3 | 125 | 25 |
| 4 | 625 | 25 |
| 5 | 3125 | 25 |

From `n = 2` onwards, the last two digits are always **25**.

So, for any `n ≥ 2`, the answer is simply **25**.

---

## Example

### Example 1
**Input:**

2


**Output:**

25


### Example 2
**Input:**

10


**Output:**

25


---
