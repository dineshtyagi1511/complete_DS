## control flow 
print("""Control Flow determines 
      the order in which statements are executed
       in a Python program.""")
print("#############")
print("IF statement ")
age = 18
if age >= 18:
    print("You are eligible to vote.")

print("#############")
print("IF - ELSE statement ")
age = 15
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

print("#############")
print("IF - ELSE -- Elif statement ")
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    


