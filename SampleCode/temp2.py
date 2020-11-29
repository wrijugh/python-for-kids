#Class declaration
class Calc:
    def __init__(self, num1, num2):
        self.i = num1 #I have created two values i,j member of the class
        self.j = num2
    
    def addition(self): #I will only pass the class here _self_ means this class
        return self.i + self.j # I use the previously created values of i & j from constructor

#Class declaration ends here
#------------------------------------

# Calling 
#You should check if user is entering correct value
x = int(input("Enter the first number: ")) 
y = int(input("Enter the first number: "))

mycalc = Calc(x, y) #See how I have initialized the Class by passing two values

result = mycalc.addition() #becuase the first parameter is self I need not pass any other values. This is already set 

print(result)