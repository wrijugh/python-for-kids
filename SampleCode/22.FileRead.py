filename = "C:\\temp\\myfile.txt"

# line = f.readline()
# print(line)
# Open file to Read 
f=open(filename,"r")
line = f.read(100) #read 100 letters 

# lines = f.read()
# print(lines)

# lines = f.readlines()
# for line in lines:
#     print(line)

# line = f.readline()
# while line != '':
#     print(line)
#     line = f.readline()
# for line in f:
#     print(line)
f.close()

#read multiple lines
# f=open(filename,"r")
# line = f.readline()
# while line != '':
#     print(line)
#     line = f.readline()

#better way to read all the line 
# for line in f:
#     print(line)
# f.close()
