# Debug Notes — Copilot Analysis

This document explains how Microsoft Copilot analyzed and improved the original script written by Jonas Joya.

---

## 1. Missing fallback for invalid fruit names

**Issue:**  
If the user typed a fruit name incorrectly, the variable `ChosenFruit` was never defined.

**Copilot Fix:**  
Added a safe fallback:
```python
else:
    ChosenPrice = 0.0
```
---

## 2. Unsafe numeric conversions

**Issue:**
The original script used float(CountFruit) and int(CountFruit) directly.
This breaks if the user enters:
- an empty string
- a decimal like "3.0"
- a non-numeric value
  
**Copilot Fix:**
Use a safe conversion:
```python
if CountFruit == "":
    Quantity = 0
else:
    Quantity = int(float(CountFruit))
```
---

## 3. Variable naming consistency

**Issue:**
ChosenFruit and ChosenPrice were mixed.

**Copilot Fix:**
Standardized to:
```python
ChosenPrice
Quantity
```
---

## 4. Code readability and structure

**Issue:**
Repeated conversions and redundant float() calls.

**Copilot Fix:**
Simplified arithmetic while respecting constraints.

---

## 5. Educational integrity
All improvements respect the original constraints:
- No imports
- No loops (except where allowed)
- No advanced Python features
- Only primitives + conditionals + arithmetic
