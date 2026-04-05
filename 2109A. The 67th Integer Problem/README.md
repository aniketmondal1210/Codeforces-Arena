# Maximize `min(x, y)`

## Problem Statement

Given an integer `x`, choose an integer `y` such that:

```
min(x, y) is maximized
```

If multiple valid `y` exist, return any.

---

# Key Observation

The function:
```
min(x, y)
```

is maximized when:

```
y ≥ x
```

Because:
- If `y ≥ x` → `min(x, y) = x` (maximum possible)
- If `y < x` → `min(x, y) = y` (smaller than x)

---

# Optimal Choice

To maximize `min(x, y)`:

```
Choose any y ≥ x
```

Simplest choice:

```
y = x + 1
```

---

# Examples

### Example 1

**Input**
```
x = 1
```

**Choose**
```
y = 2
```

```
min(1,2) = 1  (maximum possible)
```

---

### Example 2

**Input**
```
x = 3
```

**Choose**
```
y = 4
```

```
min(3,4) = 3
```

---

### Example 3

**Input**
```
x = 5
```

**Choose**
```
y = 6
```

```
min(5,6) = 5
```

---
