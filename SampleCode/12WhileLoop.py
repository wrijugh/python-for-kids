# ============================================================
# Sample        :   Day 12 - For While
# By            :   Wriju Ghosh
# Created On    :   19-Sept-2020
# Last Updated  :   
# Git Repo      :   https://github/wrijugh/python-for-kids
# ============================================================

n = 1
while n < 11:
    print(n)
    n+=1

i = 1
blnFlag = True
while blnFlag:
    print(i)
    if(i == 10):
        blnFlag = False
    i+=1

j = 1
while (j < 10):
    if(j == 5): 
        break
    else:
        print(j)
    j+=1
