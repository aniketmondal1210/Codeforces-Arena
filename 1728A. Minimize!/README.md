# Minimum Value of (c−a)+(b−c)

## Problem Statement

You are given two integers `a` and `b` (`a ≤ b`). For all possible integer values of `c` such that `a ≤ c ≤ b`, find the **minimum value** of the expression:

```
(c − a) + (b − c)
```

---

## Input

* The first line contains an integer `t` — the number of test cases.
* Each test case contains two integers `a` and `b`.

**Constraints:**

```
1 ≤ t ≤ 55
1 ≤ a ≤ b ≤ 10
```

---

## Output

For each test case, output the minimum possible value of `(c−a) + (b−c)`.

---

## Explanation

The expression can be simplified:

```
(c − a) + (b − c) = b − a
```

So the minimum possible value is always **b − a**, since it does not depend on `c`.

---

## Examples

### Example 1

**Input:**

```
3
1 2
3 10
5 5
```

**Output:**

```
1
7
0
```

**Explanation:**

* For (a, b) = (1, 2): b − a = 1
* For (a, b) = (3, 10): b − a = 7
* For (a, b) = (5, 5): b − a = 0

---

**Expected Complexity:**

* Time Complexity: **O(1)** per test case
* Space Complexity: **O(1)**

---
