Groceries=[]
TotalPrice=[]
counter= 0
def apples():
    num= int(input("How many apples do you need?"))
    TotalApples= num* 2
    TotalPrice.append(TotalApples)
    print(TotalApples, "dirhams  is the price of", num, " apples")

def bananas():
    num2= int(input("How many bananas do you need?"))
    TotalBananas= num2* 2.5
    TotalPrice.append(TotalBananas)
    print(TotalBananas, " dirhams  is the price of", num2, " bananas")

def pineapples():
    num3= int(input("How many pineapples do you need?"))
    TotalPineapples= num3* 3
    TotalPrice.append(TotalPineapples)
    print(TotalPineapples, " dirhams  is the price of", num3, " pineapples")
    
def Watermelon():
    num4= int(input("How many watermelons do you need?"))
    TotalWatermelons= num4* 5
    TotalPrice.append(TotalWatermelons)
    print(TotalWatermelons, " dirhams  is the price of", num4, " Watermelons")

def mangos():
    num5= int(input("How many mangos do you need?"))
    TotalMangos= num5* 4
    TotalPrice.append(TotalMangos)
    print(TotalMangos, " dirhams  is the price of", num5, " mangos")

while counter!= None:
    counter= input("What fruit do you want, between apple, banana, pineapple, watermelon and mango?")
    Groceries.append(counter)
    if counter == "apple" :
            apples()
    elif counter == "banana":
            bananas()
    elif counter == "pineapple":
            pineapples()
    elif counter == "watermelon":
            Watermelon()
    elif counter == "mango":
            mangos()
    else:
            break
print(Groceries)
print(TotalPrice)
print (" The total amount of money for all your groceries is " , sum(TotalPrice))
