def main():
    values = [] #2. create empty list
    #3. prompt user to enter info while using sentinel value to stop
    numbers = print("Please enter a number, press enter to quit: ")
    userInput = input("Enter the list: ")

    #4.using sentinel values while getting info
    while userInput != '': #if numbers not in values
        values.append(int(userInput))
        userInput = input("Enter another number: ")
        #7. return value to main() from step 5
    print("The list is: " ,((printNumbers(values))))

#5. get and process all info in order to get each element
# use for loop
def printNumbers(values):
    #print the sum
    sum = 0
    #this is an enhanced for loop for OOP(classes)
    for val in values:
        sum = sum + val
    print("The sum is" ,sum)
    return values

#6. send info to main() where function was called 
main() #8. end
