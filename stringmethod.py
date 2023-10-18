# String capitalize() Method
# converts first character of the string into uppercase
str = "hello python"
str2 = str.capitalize()
print(str)
print(str2)



# String Casefold() Method
# Casefold() method returns a lowercase copy of the string
str = "PYTHON"
str2 = str.casefold()
print(str)
print(str2)


# String Count() Method
# String Count() Method
str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a')
print("occurences:", oc)

str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a', 3)
print("occurences:", oc)

str = "ab bc ca de ed ad da ab bc ca"
oc = str.count('a', 3)
print("occurences:", oc)



# String find() Method
# it print its index number
string = "Hello, world!"
substring = "world"
index = string.find(substring)
print(index)


# String isalnum() Method
# to check given character is alpha-numeric character
str = "Welcome"
str2 = str.isalnum()
print(str2)



# String upper() Method
# Python upper() method converts all the character to uppercase and returns a uppercase string.
str = "anjali"
str2 = str.upper()
print(str2)


# String swapcase() Method
# Python swapcase() method converts case of the string characters from uppercase to lowercase and vice versa.
str = "HELLO PYTHON"
str2 = str.swapcase()
print (str2)


# String split() Method
# Python split() method splits the string into a comma separated list. It separates string based on the separator delimiter.
string = "Hello Wor,ld"
result = string.split("o")
print(result)


# String replace() Method
# Return a copy of the string with all occurrences of substring old replaced by new.
str = "Java is a programming language"
str2 = str.replace("Java","C")
print(str)
print(str2)



# String lower() Method
# Python lower() method returns a copy of the string after converting all the characters into lowercase.
str = "PYTHON"
str = str.lower()
print(str)



# String join() Method
lis = ['Hello', 'World', 'Python', 'Programming']
r = ' '.join(lis)
print(r)



# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))


# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"