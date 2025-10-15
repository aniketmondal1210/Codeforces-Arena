# Team Problem Solving

## Problem Statement

Three friends — **Petya**, **Vasya**, and **Tonya** — decided to form a team and participate in programming contests. They agreed that they would solve a problem **only if at least two of them are sure** about its solution.

You are given `n` problems, and for each problem, you are told whether each friend is sure about the solution (`1`) or not (`0`). Your task is to determine how many problems they will implement.

---

## Input

* The first line contains an integer `n` — the number of problems.
* The next `n` lines each contain three integers (0 or 1), representing Petya's, Vasya's, and Tonya's confidence for each problem.

**Constraints:**

```
1 ≤ n ≤ 1000
Each value is either 0 or 1
```

---

## Output

Print a single integer — the number of problems the friends will implement.

---

## Examples

### Example 1

**Input:**

```
3
1 1 0
1 1 1
1 0 0
```

**Output:**

```
2
```

**Explanation:**

```
Problem 1 → 1+1+0 = 2 (yes)
Problem 2 → 1+1+1 = 3 (yes)
Problem 3 → 1+0+0 = 1 (no)
```

They will solve 2 problems.

---

### Example 2

**Input:**

```
2
1 0 0
0 1 1
```

**Output:**

```
1
```

**Explanation:**

```
Problem 1 → 1+0+0 = 1 (no)
Problem 2 → 0+1+1 = 2 (yes)
```

They will solve only 1 problem.

---
