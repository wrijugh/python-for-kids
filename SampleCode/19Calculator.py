
class Calculator:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    # addition
    def addition(self):
        result = self.a + self.b
        print("Addition:        " + str(result))
    
    # subtraction
    def subtraction(self):
        result = self.a - self.b 
        print("Subtraction:     " + str(result))

    # multiplication
    def multiplication(self):
        result = self.a * self.b
        print("Multiplication:  " + str(result))
    
    # division
    def division(self):
        result = self.a / self.b 
        print("Division:        " + str(result))

#Calling the class 
mycalc = Calculator(20, 10)
mycalc.addition()
mycalc.subtraction()
mycalc.multiplication()
mycalc.division()
