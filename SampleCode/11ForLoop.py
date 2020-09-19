# ============================================================
# Sample        :   Day 11 - For Loop
# By            :   Wriju Ghosh
# Created On    :   18-Sept-2020
# Last Updated  :   
# Git Repo      :   https://github/wrijugh/python-for-kids
# ============================================================

# Multiplication Table
num = 5
print (1 * num)
print (2 * num)
print (3 * num)
print (4 * num)
print (5 * num)
print (6 * num)
print (7 * num)

# Multiplication Table in Intelligent way
num = 5
allNums = {1,2,3,4,5,6,7,8,9,10}
for i in allNums:
    print(i * num)

num = 5
for i in range(1,11):
    print(i * num)

# To print all the items in a Collection
nums = {1,2,3,4,5,6,7,8,9}
for i in nums:
    print(i) 

# in a string print all the letters
myname = "Wriju Ghosh"
for s in myname:
    print(s) 

# break a loop upon a condition
nums1 = {1,2,3,4,5,6,7,8,9}
for j in nums1:
    if(j == 5):
        break
    else:
        print(j)

# using range

# Start zero till 9. 10 is not included. 
for i in range(10):
    print(i)

#Start 2 and till 9. 10 is not included
for i in range(2,10):
    print(i)

# Start from 2, till 20 and take +2 for next (Step=2 - the last parameter)
for i in range(2, 21, 2):
    print(i)

# Using else range in for 
for i in range(5):
    print(i)
else:
    print("Done.")