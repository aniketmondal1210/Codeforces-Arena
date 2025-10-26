# Way Too Long Words

## Problem Statement
If a word's length is **greater than 10**, replace it with an abbreviation:

<first_letter><number_of_middle_letters><last_letter>

Otherwise, print the word as is.

---

## Example

**Input:**

4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis


**Output:**

word
l10n
i18n
p43s


---

## Explanation
- "word" → length = 4 → not changed  
- "localization" → l + 10 + n = **l10n**  
- "internationalization" → i + 18 + n = **i18n**  
- "pneumonoultramicroscopicsilicovolcanoconiosis" → p + 43 + s = **p43s**

---

## Constraints

1 ≤ n ≤ 100
1 ≤ word length ≤ 100


---
