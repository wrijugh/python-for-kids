i = num1 = input("Enter the first number: ")
j = num2 = input("Enter the second number: ")
num2 = 0
num1 = i
try:
    num2 = int(j)
except:
    print("You can only enter digits.")

class iCalculator:
    def __init__(self,num1, num2):
        self.a = i
        self.b = j

    def addition(self):
        result = num1 + num2
        print("Addition:          "  + str(result))

    def multiplication(self):
        result = num1 * num2
        print("Multiplication:    " + str(result))

mycalc = iCalculator
try:
     num2 = int(j)
     num1 = int(i)
except:
     print("Please remove the words and type only numbers.")
mycalc.addition(num2)
mycalc.multiplication(num2)
