# Define the class
class MyClass:
    a = 10
    b = 20

# Calling the MyClass 
classObject = MyClass()
#print(classObject.a) # This will print 10
#print(classObject.b) # This will print 20

# Define the class
class MyClass2:
    a = 0
    b = 0

    def initiate(self, x,y):
        self.a = x
        self.b = y

        print(self.a)
        print(self.b)

# Calling class MyClass1
classObj2 = MyClass2()
#classObj2.initiate(22,33) # This will print 22 and 33

# Define the class
class MyClass3:
    def __init__(self, x,y):
        self.a = x
        self.b = y

    def printall(self):
        print(self.a)
        print(self.b)

# Calling class MyClass1
classObj3 = MyClass3(62, 70)
#classObj3.printall() # This will print 62 and 70

# Define a blank class 
class MyClass4:
    pass

# calling dir() function
print(dir(MyClass4))
