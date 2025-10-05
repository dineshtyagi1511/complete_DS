print("FOR Loop in Python")

print("The for loop is used to iterate (repeat) over a sequence" \
" — such as a list, tuple, string, or range of numbers.")
print("??")
print("Syntax:","for variable in sequence:")
print("??")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print("################################")
print("While Loop in Python")

print("The while loop repeatedly executes a " ,
"block of code as long as a condition is True")

print("It’s mostly used when the number of iterations ",
"is not known in advance")

print("Syntax:","while condition:"
    # code block
)

count = 1

while count <= 5:
    print(count)
    count += 1  # increment to avoid infinite loop
print("""???""")
print("Break")
num = 1
while num <= 10:
    if num == 6:
        break
    print(num)
    num += 1

print("""???""")
print("Continue")

num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

print("????")
print("Enumerate")
print("Ah! enumerate() is a very handy Python built-in" \
" function used when you want to loop over a sequence "
"(like a list, tuple, or string) and get both the index "
"and the value at the same time.")
print("????")
print("Syntax:","enumerate(iterable, start=0)")
print("????")

print("""
iterable → any sequence (list, tuple, string, etc.)

start → optional, index to start counting (default is 0)

Returns an enumerate object (can be converted to a list or used in a loop)""")


fruits = ["apple", "banana", "mango"]
enumerated_fruits = list(enumerate(fruits))
print(enumerated_fruits)





