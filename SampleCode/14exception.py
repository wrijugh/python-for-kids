# ============================================================
# Sample        :   Day 14 - Exception Handling with try..except..
# By            :   Wriju Ghosh
# Created On    :   19-Sept-2020
# Last Updated  :   
# Git Repo      :   https://github/wrijugh/python-for-kids
# ============================================================
def divide(num1, num2):
    print(num1/num2)

divide(20, 2)
divide(30, 10)
divide(40, 0)
divide2(30, 15)


def divide2(num1, num2):
    if(num2!=0):
        print(num1/num2)
    else: 
        print("Can't be divided by zero")

divide2(20, 2)
divide2(30, 10)
divide2(40, 0)

def divide3(num1, num2):
    print(num1/num2)

try:
    divide3(20, 2)
except:
    print("There is an error")

try:
    divide3(40, 0)
except:
    print("There is an error")

try:
    divide3(30, 15)
except:
    print("There is an error")

def divide4(num1, num2):
    try:
        print(num1/num2)
    except:
        print("There is an error.")

divide4(10, 5)
divide4(9,0)
divide4(30,15)

#Original function
def divide5(num1, num2):
    print(num1/num2)

# Your function calling original function
def divide_error_handled(num1, num2):
    try:
        divide5(num1, num2)
    except:
        print("There is an error.")