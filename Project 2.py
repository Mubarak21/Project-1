""" The program works as a counter to determine the price of every fruit and finally to give you the total price of your purchases.
It does this by taking a function that takes Groceries as a list and The price of every fruit in the groceries list as parameters.
It asks the user to input the fruit of their choosing and then asks the amount of fruits the user needs. The program then calculates
the total amount and displays back the total price for the fruit chosen, the fruit that was chosen and how many where chosen.
I also added a loop in the program so that it can ask the user continuous until the user is satisfied."""

print("Welcome to All day, Everyday Supermarket")
Groceries= [ "Apples" , "Mango","Watermelon", "Peach", "Banana", "Orange", "Avocado", "Grape", "Pear"]# The list containing the groceries
Price= [1.25, 2.9,5,1,3,1.5,2,1.4,3]# It contains the prices of the above groceries
TotalPrice=[]# An empty list to append the prices of the fruits
Basket=[]
nFruits=[ ]

def fruits(Groceries, Price):# A function that takes the groceries and TotalPrice and calculates the total price
    for i in range (len(Groceries)):# This loops is because there only 4 fruits in the list so it runs for that many times
        if fruit == Groceries[i]:
                    num= int(input('how many fruits do you want?'))# The number of fruits that you require
                    nFruits.append(num)
                    Totalfruit= num* Price[i]# It calculates the amount of fruits that you chose
                    TotalPrice.append(Totalfruit)# It adds the prices to the empty list so that at the end of it you can get the total price
                    print(Totalfruit, ' dirhams is the price of', num, fruit)
         else:
             print("Try Again")
              fruit= input ('what fruit do you want?, either  Mango, Apples,Watermelon, Peach, Banana, Orange, Avocado, Grape, Pear')


choice= "Y"
while choice != "N":# A loop sothat the user can keep adding this to his list
            fruit= input ('what fruit do you want?, either  Mango, Apples,Watermelon, Peach, Banana, Orange, Avocado, Grape, Pear')# Asks the user what fruit they prefer
            Basket.append(fruit)
            fruits(Groceries, Price)# The function to run the calculation
            choice= input("Do you want to continue?, Y or N")


receipt= input("Do you want to print the receipt?, Yes or No")
for i in range(len(Basket)):
                        if receipt == "Yes":
                                           print(TotalPrice[i], ' dirhams is the price of', nFruits[i], fruit)

                        else:
                            print("Thank you for Visiting and Have a good day")

