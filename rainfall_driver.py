#header files

from check import Check
from rainfall import Rainfall

#driver class contains main()
def main():
    #declare a variable as a linker in order to create the object
    #call the check class
    aCheck = Check()
    dRainfall = Rainfall()

    #ask user to enter months
    months = int(input("How many months? "))
    #use a for loop to get elements
    #for i in range 12
    for i in range(months):
        #display the months with indices(index)
        print("Months# " , i + 1)
        #ask the user to enter the months
        amount = float(input("Enter the rainfall amount: "))
        #validate the amount from check file
        #link the methods in the check file
        aCheck.setQuantity(amount)
        amount = aCheck.checkQuantity()

        #connect with rainfall class
        dRainfall.inputRain(amount)

    #catch amount from rainfall class
    dRainfall.displayRain(months)

main()
