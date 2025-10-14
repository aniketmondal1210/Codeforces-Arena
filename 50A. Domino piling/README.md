# Maximum Dominoes on a Board

## Problem Statement

You are given a rectangular board of size `M × N` squares. You also have an unlimited number of standard domino pieces of size `2 × 1`. You can rotate the dominoes. You need to place as many dominoes as possible under the following conditions:

1. Each domino completely covers **two squares**.
2. No two dominoes **overlap**.
3. Each domino lies **entirely inside** the board (it can touch the edges).

Return the **maximum number** of dominoes that can be placed.

---

## Input

A single line containing two integers `M` and `N` — the dimensions of the board.

**Constraints:**

```
1 ≤ M ≤ N ≤ 16
```

---

## Output

Output a single integer — the **maximum number of dominoes** that can be placed.

---

## Examples

### Example 1

**Input:**

```
2 4
```

**Output:**

```
4
```

### Example 2

**Input:**

```
3 3
```

**Output:**

```
4
```

---
