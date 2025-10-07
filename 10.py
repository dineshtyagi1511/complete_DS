"""1️ Opening a File — open()

You use the open() function to open a file."""

#print("""Syntax:open(filename, mode)""")

""" Reading from a File """

f= open("example.txt","r")
#print(f.read())
print("???")
print(f.readline()) ## read only one line 
print("???")
print(f.readlines()) ## read all lines as a list 
f.close()

"Writing to a File"

f= open("example.txt","w")
f.write("HEllo Dinesh\n")
f.write("nahi bataunga abhi bhi ja chala ja yaha se\n")
f.close()

"Append a file"
f= open("example.txt","a")
f.write("agle line me likh be\n")

f.write("kya bangal likha h tane\n")
f.close()


"Using with Context Manager"

with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# Writing to file
with open("notes.txt", "w") as f:
    f.write("Python File Handling Example\n")
    f.write("Using read, write, and with context manager")

# Reading from file
with open("notes.txt", "r") as f:
    data = f.read()
    print(data)

