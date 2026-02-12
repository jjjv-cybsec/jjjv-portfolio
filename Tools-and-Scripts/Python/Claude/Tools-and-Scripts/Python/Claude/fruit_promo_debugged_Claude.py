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
    
# Placeholder file for Claude output
