amount = [] #create the list....this is global declaration
class Rainfall:
    #declare the Constructor-job is to initialize the attributes(variables)
    #the syntax for constructor is def __int__(self, )
    #self creates the object of the class
    def __int__(self , rain):
        #pass by value from main()
        self.rain = rain

    #make sure the quantity aka rainfall is checked from main()
    def inputRain(self , rain):
        #setting up the object
        self.rain = rain
        #getting the rainfall
        amount.append(self.rain)
    #don't forget to connect from main()
        
    #display and invoke the rain
    def displayRain(self , months):
        print("Total rainfall: %10.2f" %(sum(amount)))
        print("Average rainfall: %10.2f" %(sum(amount)/months))
        print("Highest amount: %10.2f" % max(amount))
        print("Lowest amount: %10.2f" % min(amount))
        #return amount back to main()
        return amount
    
