# Debugging Process - Original Fruit Store Code

**Author:** Grok (xAI)  
**Date:** February 2026  
**Portfolio Context:** Restricted Python exercise for Cybersecurity Career Path

### Original Code Purpose
This script calculates the total cost of a fruit purchase applying "buy more, get some free" promotions for three fruits.

### Issues Identified
1. Case-sensitive string comparison for fruit names (exact match required).
2. `print(float(CountFruit))` is a leftover debug statement with no purpose.
3. Inconsistent type conversion: `float()` used for comparison and `int()` for calculation → risk of errors or unexpected behavior with decimal input.
4. Redundant `float()` casts on already-defined price variables.
5. No handling for unrecognized fruit name → `NameError` (ChosenFruit undefined).
6. **Critical insight (user-provided context):** Quantity of fruit must be an integer (`int`) because fruits are sold as whole, countable units in this scenario (not fractional like weight or time).

### Corrected Version (conditions and promotions unchanged)

```python
# This Python code calculates three special promotions for three different fruits in a grocery store.
# NOTE: The numerical values of the currencies are Canadian dollars.
# Quantity must be whole units (int).

RedApples = 2.74
GreenPears = 1.37
YellowBananas = 0.99

FruitName = input("Enter a fruit name: ")

if FruitName == "RedApples":
    ChosenFruit = RedApples
elif FruitName == "GreenPears":
    ChosenFruit = GreenPears
elif FruitName == "YellowBananas":
    ChosenFruit = YellowBananas
else:
    ChosenFruit = 0.0
    print("Fruit not recognized")

CountFruit = input("Enter the quantity of fruit you are buying:")
Count = int(CountFruit)

if ChosenFruit == RedApples and Count > 4:
    TotalSalePromotion = (ChosenFruit * Count) - (RedApples * 1)
    print(TotalSalePromotion)
elif ChosenFruit == GreenPears and Count > 5:
    TotalSalePromotion = (ChosenFruit * Count) - (GreenPears * 1)
    print(TotalSalePromotion)
elif ChosenFruit == YellowBananas and Count > 6:
    TotalSalePromotion = (ChosenFruit * Count) - (YellowBananas * 2)
    print(TotalSalePromotion)
else:
    TotalSale = ChosenFruit * Count
    print(TotalSale)
