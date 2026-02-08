# Copilot-assisted debugging and cleanup
# Educational constraints preserved

RedApples = 2.74
GreenPears = 1.37
YellowBananas = 0.99

FruitName = input("Enter a fruit name (RedApples, GreenPears, YellowBananas): ")

if FruitName == "RedApples":
    ChosenPrice = float(RedApples)
elif FruitName == "GreenPears":
    ChosenPrice = float(GreenPears)
elif FruitName == "YellowBananas":
    ChosenPrice = float(YellowBananas)
else:
    ChosenPrice = 0.0  # Copilot fix: safe fallback

CountFruit = input("Enter the quantity of fruit you are buying: ")

if CountFruit == "":
    Quantity = 0
else:
    Quantity = int(float(CountFruit))  # Copilot fix: safe conversion

if ChosenPrice == float(RedApples) and Quantity > 4:
    TotalSale = (ChosenPrice * Quantity) - (RedApples * 1)
elif ChosenPrice == float(GreenPears) and Quantity > 5:
    TotalSale = (ChosenPrice * Quantity) - (GreenPears * 1)
elif ChosenPrice == float(YellowBananas) and Quantity > 6:
    TotalSale = (ChosenPrice * Quantity) - (YellowBananas * 2)
else:
    TotalSale = ChosenPrice * Quantity

print(TotalSale)
