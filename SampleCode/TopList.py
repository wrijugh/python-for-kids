
#Find top Large/bottom small numbers 
nums = [1,3,4,6,8,9,22,44]

#Find top 3 largest numbers 
topThree = heapq.nlargest(3, nums)
print("Three Largest..")
print(topThree)

print("")

#Find bottom 2 smallest numbers 
smallTwo = heapq.nsmallest(2, nums)
print("Two Smallest..")
print(smallTwo)

import heapq 

students = [
    {'name':'Student1', 'weight':33.5},
    {'name':'Student2', 'weight':36},
    {'name':'Student3', 'weight':35},
    {'name':'Student4', 'weight':53.5},
    {'name':'Student5', 'weight':43.5}    
]

heavyStudent = heapq.nlargest(1, students, key= lambda s : s['weight'])
print(heavyStudent)