print("##################")
print('Arithmetic Operation')

a = float(input("Enter the value of A:"))
b = float(input("Enter the value of B:"))

print("\nOperation")
print(f"Addition:{a}+{b}={a+b}") 
print(f"Subtraction:{a}-{b}={a-b}") 
print(f"Multiplication:{a}*{b}={a*b}")
print(f"Division:{a}/{b}={a/b}")
print(f"Floor_Division:{a}//{b}={a//b}")
print(f"Exponential:{a}**{b}={a**b}")
print(f"Modulus:{a}%{b}={a%b}")


print("################################################33")
print("Comparison operator")
print("""Comparison operator is used to compare two values 
and return a boolean result either true or false 
""")

print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>b:",a>b)
print("a<b:",a<b)
print("a<=b:",a<=b)
print("a>=b:",a>=b)

print("################################################33")
print("Logical operator")

a= 5
b = 6
c= 8

print(a>b and b>c)
print(a>b and b>c)
print(not a)

print("################################################")
print("Membership Operators")

print("""Membership operators are used to check if a value is 
present in a sequence (like a string, list, tuple, set, or dictionary).""")
print("a" in "apple")
print("a" not in "apple")


print("################################################")
print("Identity Operators")

print("""Identity operators are used to compare the memory location of two objects.
(They check if two variables point to the same object in memory.""")

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)       # False (different objects with same values)
print(x is z)       # True (both refer to same object)
print(x is not y)   # True
