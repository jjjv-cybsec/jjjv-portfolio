# Debugging & Refactoring: The Grocery Store Logic

**Author:** Gemini (AI) 
**Context:** This script is a debugged version of the original "Grocery Store" logic made by "Jonás joya" (GitHub user name: "jjjv-cybsec").
**Goal:** To fix potential runtime errors (like undefined variables) and optimize type conversion while strictly adhering to the "Beginner Constraints" (No functions, no loops, no libraries).

## Key Improvements made by Gemini:
1.  **Crash Prevention:** Added an `else` block to the initial input. In the original code, if a user entered a fruit name that didn't exist (e.g., "Orange"), the variable `ChosenFruit` was never created, causing the code to crash later. Now, it sets a flag `IsValid` to `0`.
2.  **Input Sanitation:** Converted `CountFruit` to an integer immediately after input. In the original, it was converted multiple times inside the logic.
3.  **Logic Simplification:** Nested the calculation inside the check for valid input to avoid errors.

## The Code

```python
# --- Configuration ---
# Price per unit (CAD)
RedApples = 2.74
GreenPears = 1.37
YellowBananas = 0.99

# Flag to control flow (since we cannot use 'exit()' or functions)
# 1 = Valid transaction, 0 = Invalid
IsValid = 1 

# --- Input Section ---
print("Available: RedApples, GreenPears, YellowBananas")
FruitName = input("Enter a fruit name: ")

# Initialize ChosenFruit with a placeholder to avoid NameError if input is wrong
ChosenFruit = 0.0

if FruitName == "RedApples":
    ChosenFruit = float(RedApples)
elif FruitName == "GreenPears":
    ChosenFruit = float(GreenPears)
elif FruitName == "YellowBananas":
    ChosenFruit = float(YellowBananas)
else:
    # Error handling within constraints
    print("Error: Unknown fruit.")
    IsValid = 0

# --- Quantity & Calculation Section ---
# Only proceed if the fruit name was valid
if IsValid == 1:
    CountInput = input("Enter the quantity of fruit you are buying: ")
    # Convert once to integer
    CountFruit = int(CountInput)
    
    print("Quantity confirmed: " + str(CountFruit))

    # Logic: Calculate Discount based on quantity thresholds
    # We use a variable 'DiscountAmount' to keep the math clean
    
    TotalSale = 0.0
    
    if FruitName == "RedApples" and CountFruit > 4:
        # Buy > 4, Get 1 Free
        # Formula: (Price * Quantity) - (Price * 1)
        TotalSale = (ChosenFruit * CountFruit) - (ChosenFruit * 1)
        print("Promotion Applied: Buy > 4 get 1 Free!")
        
    elif FruitName == "GreenPears" and CountFruit > 5:
        # Buy > 5, Get 1 Free
        TotalSale = (ChosenFruit * CountFruit) - (ChosenFruit * 1)
        print("Promotion Applied: Buy > 5 get 1 Free!")
        
    elif FruitName == "YellowBananas" and CountFruit > 6:
        # Buy > 6, Get 2 Free
        TotalSale = (ChosenFruit * CountFruit) - (ChosenFruit * 2)
        print("Promotion Applied: Buy > 6 get 2 Free!")
        
    else:
        # No promotion met
        TotalSale = ChosenFruit * CountFruit
        print("Standard pricing applied.")

    # --- Final Output ---
    print("Total to pay (CAD):")
    print(TotalSale)
