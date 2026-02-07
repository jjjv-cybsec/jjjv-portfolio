#This Python code calculates three special promotions for three different fruits in a grocery store.
#NOTE: The numerical values ​​of the currencies are Canadian dollars.
#The raw price of the fruits per unit is shown below:

RedApples = 2.74
GreenPears = 1.37
YellowBananas = 0.99

FruitName = input("Enter a fruit name: ")
if FruitName == "RedApples":
    ChosenFruit = float(RedApples)
elif FruitName == "GreenPears":
    ChosenFruit = float(GreenPears)
elif FruitName == "YellowBananas":
    ChosenFruit = float(YellowBananas)

#Here are the promotions:
#Buy more than 4 RedApples and get 1 free.
#Buy more than 5 GreenPears and get 1 free.
#Buy more than 6 YellowBananas and get 2 free.

CountFruit = input("Enter the quantity of fruit you are buying:")
print(float(CountFruit))

if ChosenFruit == float(RedApples) and float(CountFruit) > 4:
    TotalSalePromotion = (float(ChosenFruit) * int(CountFruit)) - (float(RedApples) * 1)
    print(TotalSalePromotion)
elif ChosenFruit == float(GreenPears) and float(CountFruit) > 5:
    TotalSalePromotion = (float(ChosenFruit) * int(CountFruit)) - (float(GreenPears) * 1)
    print(TotalSalePromotion)
elif ChosenFruit == float(YellowBananas) and float(CountFruit) > 6:
    TotalSalePromotion = (float(ChosenFruit) * int(CountFruit)) - (float(YellowBananas) * 2)
    print(TotalSalePromotion)
else:
    TotalSale = float(ChosenFruit) * int(CountFruit)
    print(TotalSale)
