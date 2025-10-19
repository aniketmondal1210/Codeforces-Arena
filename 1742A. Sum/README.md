# Check if One Number is the Sum of the Other Two

## Problem Statement
You are given three integers `a`, `b`, and `c`.  
Determine if **one of them is the sum of the other two**.

---

## Input
- The first line contains an integer `t` — the number of test cases.  
- Each test case contains three integers `a`, `b`, and `c`.

**Constraints:**

1 ≤ t ≤ 9261
0 ≤ a, b, c ≤ 20


---

## Output
For each test case, output:
- `"YES"` if one of the numbers is the sum of the other two.
- `"NO"` otherwise.

Output can be in any letter case (e.g., `Yes`, `yEs`, `YES` are all valid).

---

## Explanation
We need to check if:

a + b == c OR a + c == b OR b + c == a

If any of these conditions hold true, print `"YES"`. Otherwise, print `"NO"`.

---

## Examples

### Example 1
**Input:**

7

1 4 3

2 5 8

9 11 20

0 0 0

20 20 20

4 12 3

15 7 8

**Output:**

YES

NO

YES

YES

NO

NO

YES

**Explanation:**
- (1, 4, 3) → 1 + 3 = 4 → YES  
- (2, 5, 8) → none of the sums match → NO  
- (9, 11, 20) → 9 + 11 = 20 → YES  
- (0, 0, 0) → 0 + 0 = 0 → YES  
- (20, 20, 20) → no number equals sum of others → NO  
- (4, 12, 3) → none match → NO  
- (15, 7, 8) → 7 + 8 = 15 → YES  

---
