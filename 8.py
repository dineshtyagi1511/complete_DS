#A = input("Enter Your Name:")
#B = input("Enter Your Age:")


#print(f"MY name is {A} and my Age is {B}")


text = "Dinesh"
print(text.upper())
print(text.lower())

## .strip()

## Removes extra spaces (or specified characters)
#  from the beginning and end of a string.

text = "         Dinesh  "
print(text)

print(text.strip())

text = "333333dinesh3333"
print(text)
print(text.strip("3"))

""".split()

Splits a string into a 
list of words based on a separator (default is space)."""

text = "MY name is  keshav tyagi"
print(text.split())
print(text.split("m"))

""".join()

Joins elements of a list into a single string using a separator."""

sentence = " ".join(text.split())
print(sentence)

sentence = " ?? ".join(text.split())
print(sentence)

""""Slicing:

Extract a part (substring) of a string using [start:end:step]."""

word = "Python"
print(word[0:4])   
print(word[:3])    
print(word[2:])    
print(word[::-1])  

