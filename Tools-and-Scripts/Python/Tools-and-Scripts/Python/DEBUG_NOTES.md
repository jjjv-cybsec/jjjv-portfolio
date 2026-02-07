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
