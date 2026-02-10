# Debugging Process – Fruit Promotion Algorithm (Beginner Python)

## Context
This Python script was created as a beginner-level exercise based on the concepts learned in **Python for Everybody (University of Michigan)**.

The objective was to calculate promotional discounts for a grocery store using **strict constraints**:
- Only `str`, `int`, `float`.
- Variables.
- `if / elif / else`.
- Arithmetic operators.
- No functions, no libraries, no advanced Python features.

The goal of this debugging process is **not to redesign the solution**, but to analyze edge cases, logical risks, and improvement opportunities **while respecting all constraints**.

---

## 1. Input Validation Risk

### Issue
The program assumes the user will always type:
- A valid fruit name.
- A numeric quantity.

If the user enters an unexpected value (e.g. lowercase name or non-numeric quantity), the program may crash or behave unexpectedly.

### Why it happens
- `input()` always returns a string.
- The code converts values directly to `float` or `int` without validation.

### Educational Insight
At a beginner level, this is acceptable.
At higher levels, input validation would be added using loops or error handling (which are intentionally excluded here).

---

## 2. Case Sensitivity in Fruit Selection

### Issue
The comparison:
```python
if FruitName == "RedApples":
```

- Requires an exact match.
- Typing "redapples" or "Red Apples" will not work.

### Why it happens
String comparison in Python is case-sensitive by default.

### Educational Insight
This reinforces the importance of data normalization, which is a key concept in both programming and cybersecurity.

---

## 3. Type Conversion Redundancy

### Observation
Some values are converted multiple times:
```python                                          
float(ChosenFruit)
int(CountFruit)
```

### Why this is acceptable
- This is a conscious trade-off to stay within beginner constraints.
- It reinforces understanding of type conversion.   

---

## 4. Promotion Logic Verification
                                                    
### Strength
Each promotion rule is correctly implemented using:
- Conditional logic.
- Arithmetic subtraction for free items.

Example:
```python
TotalSalePromotion = (ChosenFruit * CountFruit) - (RedApples * 1)
```

### Educational Value
This shows a solid grasp of:
- Conditional branching.
- Real-world logic modeling.
- Arithmetic operations without helper functions.

---

# Conclusion

This script demonstrates:
- Clear logical thinking.
- Correct use of beginner Python constructs.
- Intentional design under strict constraints

The limitations are educational by design, not mistakes.
This makes the code ideal for learning, refactoring exercises, and recontextualization.
