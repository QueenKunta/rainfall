class Check:
    #declare the Constructor-job is to initialize the attributes(variables)
    #the syntax for constructor is def __int__(self, )
    #self creates the object of the class
    def __int__(self , quantity):
        #pass by value from main()
        self.quantity = quantity

    #make sure the quantity aka rainfall is checked from main()
    def setQuantity(self , quantity):
        self.quantity = quantity

    #input validation (trash)
    def checkQuantity(self):
        counter = 0
        while True:
            try:
                if counter < 1:
                    value = float(self.quantity)

                else:
                    value = float(input("Please try entering the rainfall again."))

                while value < 0:
                    print("Invalid input.")
                    value = float(input("Please try entering the rainfall again."))

            except ValueError:
                #reset to if statement
                counter = counter + 1
                print("Try again bruh.")
                continue

            else:
                break

        return value
        
    
    
