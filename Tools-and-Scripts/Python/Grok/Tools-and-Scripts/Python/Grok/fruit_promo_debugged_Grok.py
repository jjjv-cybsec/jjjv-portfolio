# Debugging Process - Original Code (Fruit Shop)

**Author:** Grok (xAI)
**Date:** February 2026
**Objective:** Analyze and correct the original code without modifying the original **promotion conditions**.

### Original Code (Summary)
The script asks for a fruit name and quantity, then applies one of these promotions:
- RedApples → more than 4 → 1 free
- GreenPears → more than 5 → 1 free
- YellowBananas → more than 6 → 2 free

### Problems Found
1. **Case sensitivity** and exact string matching.
2. `print(float(CountFruit))` is a useless debugging remnant.
3. Inconsistent conversion (`float` in one part, `int` in another) → possible error if a decimal is entered.
4. Redundancy of `float()` across multiple lines.
5. If an invalid fruit is entered → `NameError` (ChosenFruit not defined).
6. No basic handling of invalid input (although with the restrictions it is limited).

### Corrected code (maintaining exactly the same conditions)

```python
# This Python code calculates three special promotions for three different fruits in a grocery store.
# NOTE: The numerical values of the currencies are Canadian dollars.

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
Count = float(CountFruit)

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
