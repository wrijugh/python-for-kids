# ============================================================
# Sample        :   Day 7 - Strings in Detail
# By            :   Wriju Ghosh
# Created On    :   16-Sept-2020
# Last Updated  :   17-Sept-2020
# Git Repo      :   https://github.com/wrijugh/python-for-kids
# ============================================================
s = "Hello World"
# all upper or capital
x = s.upper()
print(x)

# make all lower 
y = s.lower()
print(y)

# change upper to lower and lower to upper
z = s.swapcase()
print(z)

ss = "all the letters are small and we need to make it title case"
print(ss.title())

#String is array
print(s[0])

#Length 
print(len(s))

#string removing space before and after
s1 = "   Space before and after      "
print(s1)
print(s1.strip())

#replace 
s2 = s.replace("H", "K")
print(s2)

#Multiline 
mult = """This is a sample of 
multiple line text which is otherwise hard
to read in single line."""
print(mult)

#Split 
s = "Hello, world"
arr = s.split(',')
print(arr)

#Search a phrase in a string 
bigstring = "The big string would contain a lot of words and it is hard to find if a single word is available"
x = "rd" in bigstring
print(x)

#String format
# placing
name = "Wriju Ghosh"
phone = "123-456-7890"
email = "wriju@contoso.com"

msg = "Call {} at {} or send email to {}."
print(msg.format(name,phone, email)) # Then need to follow seq 

# if seq is predecided 
msg2 = "Call {2} at {0} or send email at {1}"
print(msg2.format(phone, email, name)) # place them as per the sequence

# escape 
#how will you have a string with doubel quote inside 
s4 = "He said, \"Hello Everyone\""
print(s4)