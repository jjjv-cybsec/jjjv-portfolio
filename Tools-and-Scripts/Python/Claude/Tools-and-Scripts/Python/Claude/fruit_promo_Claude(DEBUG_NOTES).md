# Debug Notes - Original Code Analysis

## Code Review by Claude AI

### Original Code Context
This debugging analysis reviews the original Python fruit store promotion calculator, which was created with beginner-level Python constraints from the University of Michigan's "Python for Everybody" course.

---

## Issues Found and Fixes

### 🐛 Bug #1: Missing Error Handling for Invalid Fruit Names

**Problem:**
```python
FruitName = input("Enter a fruit name: ")
if FruitName == "RedApples":
    ChosenFruit = float(RedApples)
elif FruitName == "GreenPears":
    ChosenFruit = float(GreenPears)
elif FruitName == "YellowBananas":
    ChosenFruit = float(YellowBananas)
```

If the user enters anything other than the exact fruit names (e.g., "redapples", "Bananas", or "Orange"), the variable `ChosenFruit` is never defined, causing a **NameError** in later comparisons.

**Fix:**
```python
FruitName = input("Enter a fruit name: ")
if FruitName == "RedApples":
    ChosenFruit = float(RedApples)
elif FruitName == "GreenPears":
    ChosenFruit = float(GreenPears)
elif FruitName == "YellowBananas":
    ChosenFruit = float(YellowBananas)
else:
    ChosenFruit = 0.0
    print("Invalid fruit name. Please enter: RedApples, GreenPears, or YellowBananas")
```

---

### 🐛 Bug #2: Unnecessary Float Conversions

**Problem:**
```python
if ChosenFruit == float(RedApples) and float(CountFruit) > 4:
```

The code repeatedly converts already-float values (`RedApples`, `GreenPears`, `YellowBananas`) to float, and converts `CountFruit` multiple times in each conditional.

**Impact:** Inefficient code execution and harder readability.

**Fix:**
```python
CountFruitInt = int(CountFruit)
CountFruitFloat = float(CountFruit)

if ChosenFruit == RedApples and CountFruitFloat > 4:
    TotalSalePromotion = (ChosenFruit * CountFruitInt) - (RedApples * 1)
    print(TotalSalePromotion)
```

---

### 🐛 Bug #3: Print Statement Without Context

**Problem:**
```python
CountFruit = input("Enter the quantity of fruit you are buying:")
print(float(CountFruit))
```

This prints the quantity without explanation, which may confuse users.

**Fix:**
```python
CountFruit = input("Enter the quantity of fruit you are buying: ")
print("Quantity entered: " + CountFruit)
```

Or using string formatting within constraints:
```python
print("You are buying " + CountFruit + " units")
```

---

### 🐛 Bug #4: No Validation for Negative or Zero Quantities

**Problem:**
The code accepts any numeric input, including negative numbers or zero, which doesn't make sense for a purchase.

**Fix:**
```python
CountFruit = input("Enter the quantity of fruit you are buying: ")
CountFruitFloat = float(CountFruit)

if CountFruitFloat <= 0:
    print("Error: Quantity must be greater than zero")
    TotalSale = 0.0
else:
    # Continue with normal logic
```

---

### 🐛 Bug #5: Inconsistent Variable Usage

**Problem:**
The code sometimes uses `int(CountFruit)` and sometimes `float(CountFruit)` in calculations, which could lead to confusion about data types.

**Fix:**
Assign converted values once at the beginning:
```python
CountFruitInt = int(CountFruit)
CountFruitFloat = float(CountFruit)
```

Then use the appropriate version consistently.

---

## Complete Debugged Version

```python
#This Python code calculates three special promotions for three different fruits in a grocery store.
#NOTE: The numerical values of the currencies are Canadian dollars.
#The raw price of the fruits per unit is shown below:

RedApples = 2.74
GreenPears = 1.37
YellowBananas = 0.99

FruitName = input("Enter a fruit name (RedApples, GreenPears, or YellowBananas): ")
if FruitName == "RedApples":
    ChosenFruit = RedApples
elif FruitName == "GreenPears":
    ChosenFruit = GreenPears
elif FruitName == "YellowBananas":
    ChosenFruit = YellowBananas
else:
    ChosenFruit = 0.0
    print("Invalid fruit name entered")

#Here are the promotions:
#Buy more than 4 RedApples and get 1 free.
#Buy more than 5 GreenPears and get 1 free.
#Buy more than 6 YellowBananas and get 2 free.

CountFruit = input("Enter the quantity of fruit you are buying: ")
CountFruitFloat = float(CountFruit)
CountFruitInt = int(CountFruit)

print("You are buying " + CountFruit + " units")

if CountFruitFloat <= 0:
    print("Error: Quantity must be greater than zero")
    print(0.0)
elif ChosenFruit == 0.0:
    print("Cannot calculate total - invalid fruit selected")
    print(0.0)
elif ChosenFruit == RedApples and CountFruitFloat > 4:
    TotalSalePromotion = (ChosenFruit * CountFruitInt) - (RedApples * 1)
    print("Promotion applied! Total: $" + str(TotalSalePromotion))
elif ChosenFruit == GreenPears and CountFruitFloat > 5:
    TotalSalePromotion = (ChosenFruit * CountFruitInt) - (GreenPears * 1)
    print("Promotion applied! Total: $" + str(TotalSalePromotion))
elif ChosenFruit == YellowBananas and CountFruitFloat > 6:
    TotalSalePromotion = (ChosenFruit * CountFruitInt) - (YellowBananas * 2)
    print("Promotion applied! Total: $" + str(TotalSalePromotion))
else:
    TotalSale = ChosenFruit * CountFruitInt
    print("Total: $" + str(TotalSale))
```

---

## Summary

The original code demonstrated solid understanding of conditional logic and basic Python operations within the specified constraints. The main issues were:

1. **Crash potential** from undefined variables when invalid input is provided
2. **Inefficiency** from repeated type conversions
3. **User experience** gaps in error messaging and validation
4. **Edge cases** not handled (negative quantities, zero quantities)

All fixes maintain the original constraints: no imports, no advanced functions, only basic conditionals, variables, and arithmetic operators.

---

## Testing Recommendations

Test these scenarios:
- Valid fruit names with quantities that trigger promotions
- Valid fruit names with quantities below promotion threshold
- Invalid fruit names
- Zero quantity
- Negative quantity
- Non-numeric quantity input (will cause ValueError - expected within constraints)

---

**Analysis completed by:** Claude AI (Anthropic)  
**Date:** February 2026  
**Constraint compliance:** ✅ All fixes respect original limitations
