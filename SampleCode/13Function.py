# ============================================================
# Sample        :   Day 13 - Function
# By            :   Wriju Ghosh
# Created On    :   19-Sept-2020
# Last Updated  :   
# Git Repo      :   https://github/wrijugh/python-for-kids
# ============================================================

def addition(num1, num2):
    print(num1 + num2)

addition(10,20)

# simple function
def my_function():
    print("You called me!")

my_function()

# with parameter
def my_function2(myname):
    print("Hello from " + myname)

my_function2("Wriju")

#Two parameters and return type
def my_function3(firstname, lastname):
    return "Hello from " + firstname + " " + lastname
#passing parameter in exact sequence 
print(my_function3("Wriju", "Ghosh"))

#calling parameter by name
print(my_function3(lastname="Tagore", firstname = "Rabindranath"))

#do nothing function
def my_function4():
    pass

#default parameter value, when not supplied the default will show. 
def my_function5(myname = "No Name!!!"):
    print("My name is : " + myname)

my_function5("Wrishika")    # call with a parameter value
my_function5()              # call without a parameter value