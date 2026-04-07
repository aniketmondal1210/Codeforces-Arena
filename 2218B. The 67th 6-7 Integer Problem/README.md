# Negate 6 Elements to Maximize Sum

## Problem Statement

You are given **7 integers**:

```
a1, a2, a3, a4, a5, a6, a7
```

You must **negate exactly 6 elements** (multiply by `-1`) and leave **only one element unchanged**.

Your task is to find the **maximum possible sum** after performing this operation.

---

# Key Insight

Let:

```
Total sum = S = a1 + a2 + ... + a7
```

If you negate 6 elements and keep one element `x` unchanged:

```
New Sum = x - (S - x)
         = 2x - S
```

---

# Goal

Maximize:

```
2x - S
```

Since `S` is constant, we just need to:

```
Choose the maximum element x
```

---

# Final Formula

```
Answer = 2 * (max element) - (sum of all elements)
```

---

# Examples

### Example 1

**Input**
```
41 41 41 41 41 41 41
```

```
S = 287
max = 41
Answer = 2*41 - 287 = -205
```

---

### Example 2

**Input**
```
6 9 4 20 6 7 67
```

```
S = 119
max = 67
Answer = 2*67 - 119 = 15
```

---

### Example 3

**Input**
```
1 2 3 4 5 6 7
```

```
S = 28
max = 7
Answer = 2*7 - 28 = -14
```

---
