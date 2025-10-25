# Next Round — Contest Qualification Problem

## Problem Statement
You are given the scores of `n` contestants in non-increasing order.  
A contestant will **advance to the next round** if:
- Their score is **at least equal** to the score of the **k-th place finisher**, and  
- Their score is **positive**.

You must calculate **how many contestants will advance**.

---

## Input
- First line: Two integers `n` and `k`  
  `(1 ≤ k ≤ n ≤ 50)`
- Second line: `n` space-separated integers  
  `a₁, a₂, ..., aₙ` where `(0 ≤ aᵢ ≤ 100)`  
  Scores are given in **non-increasing order**.

---

## Output
- A single integer — number of participants who will advance.

---

## Example 1
**Input**

8 5
10 9 8 7 7 7 5 5

**Output**

6

**Explanation**
The 5th place score = `7`.  
All contestants with scores `≥ 7` and `> 0` advance.  
Hence, 6 contestants advance.

---

## Example 2
**Input**

4 2
0 0 0 0

**Output**

0

**Explanation**
No contestant has a positive score.

---
