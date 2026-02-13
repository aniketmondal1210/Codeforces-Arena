# Print N Distinct Perfect Roots

## Problem Statement

A positive integer `x` is called a **perfect root** if there exists an integer `y` such that:



√y = x


In other words:



y = x²


So any positive integer `x` is a perfect root because its square is an integer.

For each test case, you need to output `n` **distinct perfect roots**.

- The values only need to be distinct **within a single test case**.
- The same values can be reused across different test cases.
- Each value must satisfy:


1 ≤ x ≤ 10⁹


---

## Input Format

- First line contains integer `t` — number of test cases  


1 ≤ t ≤ 20

- Each test case contains one integer `n`  


1 ≤ n ≤ 20


---

## Output Format

For each test case, output `n` distinct perfect roots.

---

## Example

### Input


3
1
2
5


### Output


1
2 4
2 102 43 1 21


---

## Explanation

- `1` is a perfect root because:


√1 = 1


- `2` is a perfect root because:


√4 = 2


- `4` is a perfect root because:


√16 = 4


---
