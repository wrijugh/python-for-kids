# Write to a file 
filename = "C:\\temp\\myfile.txt"
f=open(filename,"w")
f.write("Hello from code to write to a file.")
f.close()


def readFile(filename):
    f=open(filename,"r")
    for line in f:     
        print(line)
    f.close()

filename = "C:\\temp\\myfile2.txt"
f = open(filename, "w")
lines = ["Line1\n", "Line2\n", "Line3\n"]
f.writelines(lines)
f.close()

readFile(filename)


