# standard assignment
name = "Valerio"
age = 32
is_attractive = True  # lol

print("Standard assignment")
print(name)
print(age)
print(is_attractive)
print()

# multiple assignment

name, age, is_attractive = "Valerio 2", 23, False

print("Multiple assignment")
print(name)
print(age)
print(is_attractive)
print()

# string methods

print("String methods section")
name = "Valerio"
word = "ciao"
numbers_string = "123"

print("The length is:", len(name))
print(name.find("r"))  # returns the index position (starting from 0) of that letter
print(name.find("a"))

print(word.capitalize())  # return the capitalized string
print(name.upper())  # returns all uppercase
print(name.lower())  # all lowercase

print()
print("Is digit:")
print(name.isdigit())  # isdigit is boolean, returns true if thw string is made by digits
print(numbers_string.isdigit())

print()
print("Is alpha:")
print(name.isalpha())  # true if there are only letters (spaces makes also return false, they are no alphas)
print(numbers_string.isalpha())

print()
print("Count:")  # counts how many times the passed value is in the string
print(name.count("a"))
print(name.count("z"))

print()
print("Replace:")  # replaces the first string passed with the second
print(name.replace("V", "Z"))
print(name.replace("vale".capitalize(), "ma".capitalize()))  # you can use methods directly on strings like here
print(name.replace("vale".capitalize(), "ma".capitalize()).upper())

print()
print("Multiple of the same string:")  # you can display the same string multiple times
print(name*3)
print((name*5).upper())
print(((name + " ")*5).upper())

print()
print("User input section")

text = input("Enter your name: ")
print("My name is: " + text)

text = input("How old are you?: ")
print ("I am " + str(text))

